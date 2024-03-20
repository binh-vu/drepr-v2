from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest
import serde.yaml

from drepr.utils.udf import SourceTree, UDFParsedResult, UDFParser


@dataclass
class UDFTestCase:
    name: str
    code: str
    monitor_vars: dict[str, bool]
    imports: list[str]
    norm_code: list | dict

    @staticmethod
    def get_norm_code(tree: SourceTree) -> list | dict:
        children = [
            child.get_simplified_dict() if len(child.children) > 0 else child.node
            for child in tree.children
        ]

        if tree.node == "":
            return children

        return {
            "node": tree.node,
            "children": children,
        }


@pytest.fixture
def udf_test_cases(resource_dir: Path) -> list[UDFTestCase]:
    def recover_newline(code: list | dict):
        if isinstance(code, list):
            return [recover_newline(c) for c in code]
        if isinstance(code, dict):
            return {k: recover_newline(v) for k, v in code.items()}
        return code.replace("\\n", "\n")

    testcases = []
    for file in sorted((resource_dir / "udf").iterdir()):
        if file.suffix in {".yaml", ".yml"}:
            obj = serde.yaml.deser(file)
            for name, testcase in obj.items():
                testcases.append(
                    UDFTestCase(
                        name=name,
                        code=testcase["code"],
                        imports=testcase.get("imports", []),
                        monitor_vars=testcase.get("monitor_vars", {}),
                        norm_code=recover_newline(testcase["norm"]),
                    )
                )
    return testcases


def test_norm_prefix_space(udf_test_cases: list[UDFTestCase]):
    # print(">>>")
    for testcase in udf_test_cases:
        # print(testcase.code)
        res = UDFParser(testcase.code).parse(list(testcase.monitor_vars.keys()))
        # print(UDFTestCase.get_norm_code(res.source_tree))
        assert UDFTestCase.get_norm_code(res.source_tree) == testcase.norm_code
        assert res.imports == testcase.imports
        assert res.monitor_variables == {
            k for k, v in testcase.monitor_vars.items() if v
        }
