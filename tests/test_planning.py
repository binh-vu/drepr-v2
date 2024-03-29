from __future__ import annotations

import json

import orjson
import pytest
import serde.json

from drepr.models.prelude import DRepr
from drepr.planning.class_map_plan import BlankSubject, ClassesMapExecutionPlan, Subject
from tests.conftest import DatasetExample


@pytest.mark.parametrize("name", ["pseudo_people"])
def test_planning(name, example_datasets: dict[str, DatasetExample]):
    ds = example_datasets[name]
    model = DRepr.parse_from_file(ds.model)

    plan = ClassesMapExecutionPlan.create(model)

    serplan = [
        {
            "class_id": plan.class_id,
            "subject": subj_to_json(plan.subject),
            "data_props": [
                {
                    "predicate": p.predicate,
                    "attr": p.attr.id,
                    "is_optional": p.is_optional,
                }
                for p in plan.data_props
            ],
            "literal_props": [
                {
                    "predicate": p.predicate,
                    "value": p.value,
                }
                for p in plan.literal_props
            ],
            "object_props": [
                {
                    "predicate": p.predicate,
                    "attr": p.attr.id,
                    "class_id": p.class_id,
                    "is_optional": p.is_optional,
                    "can_target_missing": p.can_target_missing,
                }
                for p in plan.object_props
            ],
            "buffered_object_props": [
                {
                    "predicate": p.predicate,
                    "attr": p.attr.id,
                    "class_id": p.class_id,
                    "is_optional": p.is_optional,
                    "can_target_missing": p.can_target_missing,
                }
                for p in plan.buffered_object_props
            ],
        }
        for plan in plan.class_map_plans
    ]

    # serde.json.ser(
    #     serplan, ds.cwd / f"{ds.model.stem.split('.')[0]}.plan.json", indent=2
    # )
    assert serplan == serde.json.deser(ds.cwd / f"program/plan.json")


def subj_to_json(subj: Subject):
    if isinstance(subj, BlankSubject):
        return {
            "attr": subj.attr.id,
        }
    return {
        "attr": subj.attr.id,
        "is_optional": subj.is_optional,
    }
