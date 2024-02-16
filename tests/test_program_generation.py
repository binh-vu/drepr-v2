from __future__ import annotations

import json

import orjson
import pytest
import serde.json

from drepr.models.prelude import DRepr, OutputFormat
from drepr.planning.class_map_plan import BlankSubject, ClassesMapExecutionPlan, Subject
from drepr.program_generation.main import MemoryOutput, gen_program
from tests.conftest import DatasetExample


@pytest.mark.parametrize("name", ["pseudo_people/s01"])
def test_program_generation(name, example_datasets: dict[str, DatasetExample]):
    ds = example_datasets[name]
    model = DRepr.parse_from_file(ds.model)

    plan = ClassesMapExecutionPlan.create(model)
    prog = gen_program(model, plan, MemoryOutput(OutputFormat.TTL)).to_python()

    assert prog == (ds.cwd / f"{ds.model.stem.split('.')[0]}.py").read_text()
