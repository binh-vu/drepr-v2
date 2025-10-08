from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
from drepr.models.prelude import DRepr, OutputFormat
from drepr.planning.class_map_plan import ClassesMapExecutionPlan
from drepr.program_generation.main import FileOutput, MemoryOutput, gen_program
from rdflib import Graph, compare
from tests.conftest import DatasetExample


@pytest.mark.parametrize(
    "name",
    [
        "pseudo_people",
        "mineral_site/missing_values",
        "mineral_site/invalid_variable_names",
        "mineral_system/misspath_autoalign",
        "resource_categories",
    ],
)
def test_program_generation(
    name, example_datasets: dict[str, DatasetExample], tmp_path: Path
):
    ds = example_datasets[name]
    model = DRepr.parse_from_file(ds.model)

    plan = ClassesMapExecutionPlan.create(model)

    prog = gen_program(
        model, plan, MemoryOutput(OutputFormat.TTL), debuginfo=False
    ).to_python()
    if not (ds.cwd / f"program/write_to_str.py").exists():
        (ds.cwd / f"program/write_to_str.auto.py").write_text(prog)

    if prog != (ds.cwd / f"program/write_to_str.py").read_text():
        (ds.cwd / f"program/write_to_str.auto.py").write_text(prog)
        pytest.fail(
            "The generated program is different from the expected program. Please check the file: program/write_to_str.auto.py"
        )

    prog = gen_program(
        model,
        plan,
        FileOutput(tmp_path / f"{ds.name}.ttl", OutputFormat.TTL),
        debuginfo=False,
    ).to_python()
    if not (ds.cwd / f"program/write_to_file.py").exists():
        (ds.cwd / f"program/write_to_file.auto.py").write_text(prog)
    if prog != (ds.cwd / f"program/write_to_file.py").read_text():
        (ds.cwd / f"program/write_to_file.auto.py").write_text(prog)
        pytest.fail(
            "The generated program is different from the expected program. Please check the file: program/write_to_file.auto.py"
        )

    # now invoke the generated program and compare the output
    spec = importlib.util.spec_from_file_location(
        "drepr_prog", (ds.cwd / f"program/write_to_str.py")
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    output = module.main(*[ds.resources[r.id] for r in model.resources])
    # (ds.cwd / "tmp.ttl").write_text(output)
    gold_g = Graph()
    gold_g.parse(data=output)

    pred_g = Graph()
    pred_g.parse(data=ds.output.read_text())
    # x, y, z = compare.graph_diff(gold_g, pred_g)
    # print(list(x), list(y), list(z))

    assert compare.isomorphic(
        gold_g, pred_g
    ), "The output of the generated program is different from the expected output"
