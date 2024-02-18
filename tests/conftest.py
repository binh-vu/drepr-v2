from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest


@dataclass
class DatasetExample:
    name: str
    model: Path
    resources: dict[str, Path]
    cwd: Path


@pytest.fixture
def example_datasets() -> dict[str, DatasetExample]:
    def norm_example(dir: Path) -> DatasetExample:
        model = dir / "model.yml"
        return DatasetExample(
            name=dir.name,
            model=dir / "model.yml",
            resources={
                file.stem: file
                for file in dir.iterdir()
                if file.is_file()
                and not file.name.startswith(".")
                and file.name != "model.yml"
            },
            cwd=dir,
        )

    def find_examples(basedir: Path, current_dir: Path, out: dict[str, DatasetExample]):
        for dir in current_dir.iterdir():
            if not dir.is_dir() or (dir / ".ignore").exists():
                continue

            if (dir / "model.yml").exists():
                out[str(dir.relative_to(basedir))] = norm_example(dir)
                continue
            else:
                find_examples(basedir, dir, out)

    example_dir = Path(__file__).parent.parent / "examples"
    examples = {}
    find_examples(example_dir, example_dir, examples)
    return examples
