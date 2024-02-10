from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest


@dataclass
class DatasetExample:
    model: Path
    resources: dict[str, str]
    cwd: Path


@pytest.fixture
def example_datasets() -> dict[str, DatasetExample]:
    examples = {}
    for dir in (Path(__file__).parent.parent / "examples").iterdir():
        if not dir.is_dir() or (dir / ".ignore").exists():
            continue

        # one folder may have multiple examples
        models = [file for file in dir.iterdir() if file.name.endswith("model.yml")]

        for model in models:
            dsid = model.stem.split(".")[0]
            resources = {}
            for file in dir.iterdir():
                if file.stem.startswith(dsid) and not file.stem.startswith(
                    f"{dsid}.model"
                ):
                    resources[file.stem[len(dsid) + 1 :]] = str(file)

            full_dsid = f"{dir.name}/{dsid}"
            assert full_dsid not in examples
            examples[full_dsid] = DatasetExample(
                model=model,
                resources=resources,
                cwd=dir,
            )
    return examples
