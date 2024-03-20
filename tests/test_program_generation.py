from __future__ import annotations

import json
from pathlib import Path

import orjson
import pytest
import serde.json

from drepr.models.prelude import DRepr, OutputFormat
from drepr.planning.class_map_plan import BlankSubject, ClassesMapExecutionPlan, Subject
from drepr.program_generation.main import FileOutput, MemoryOutput, gen_program
from tests.conftest import DatasetExample


@pytest.mark.parametrize(
    "name",
    [
        "pseudo_people",
        "mineral_site/missing_values",
        "mineral_system/misspath_autoalign",
        "resource_categories",
    ][-1:],
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
    assert prog == (ds.cwd / f"program/write_to_str.py").read_text()

    prog = gen_program(
        model,
        plan,
        FileOutput(tmp_path / f"{ds.name}.ttl", OutputFormat.TTL),
        debuginfo=False,
    ).to_python()
    if not (ds.cwd / f"program/write_to_file.py").exists():
        (ds.cwd / f"program/write_to_file.auto.py").write_text(prog)
    assert prog == (ds.cwd / f"program/write_to_file.py").read_text()
