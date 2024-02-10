from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest


@dataclass
class DatasetExample:
    models: Path
    resources: dict[str, str]
    cwd: Path


@pytest.fixture
def examples():
    examples = []
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

            examples.append(
                DatasetExample(
                    models=model,
                    resources=resources,
                    cwd=dir,
                )
            )
    return examples
