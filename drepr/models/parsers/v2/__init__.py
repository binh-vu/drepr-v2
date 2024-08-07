from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
from typing import TYPE_CHECKING, List

from drepr.models.align import AlignmentType, RangeAlignment
from drepr.models.parsers.v1.align_parser import AlignParser
from drepr.models.parsers.v1.attr_parser import AttrParser, ParsedAttrs
from drepr.models.parsers.v1.preprocessing_parser import PreprocessingParser
from drepr.models.parsers.v1.resource_parser import ResourceParser
from drepr.models.parsers.v2.path_parser import PathParserV2
from drepr.models.parsers.v2.sm_parser import SMParser
from drepr.models.sm import ClassNode, DataNode, LiteralNode, SemanticModel
from drepr.utils.validator import *

if TYPE_CHECKING:
    from drepr.models.drepr import DRepr


class ReprV2Parser:
    """
    The D-REPR language version 2 has similar to the schema of the first version.

    Difference with previous features:
    1. For spreadsheet columns, they can the letter instead of number
    2. Semantic model configuration is changed to focus on classes
    """

    TOP_KEYWORDS = {
        "version",
        "resources",
        "preprocessing",
        "attributes",
        "alignments",
        "semantic_model",
    }
    DEFAULT_RESOURCE_ID = "default"

    @classmethod
    def parse(cls, raw: dict):
        from drepr.models.drepr import DRepr

        Validator.must_be_subset(
            cls.TOP_KEYWORDS,
            raw.keys(),
            setname="Keys of D-REPR configuration",
            error_msg="Parsing D-REPR configuration",
        )

        for prop in ["version", "resources", "attributes"]:
            Validator.must_have(raw, prop, error_msg="Parsing D-REPR configuration")

        Validator.must_equal(
            raw["version"], "2", "Parsing D-REPR configuration version"
        )
        resources = ResourceParser.parse(raw["resources"])
        attrs = ParsedAttrs()

        if len(resources) == 1:
            default_resource_id = resources[0].id
        else:
            default_resource_id = ResourceParser.DEFAULT_RESOURCE_ID

        path_parser = PathParserV2()
        preprocessing = PreprocessingParser(path_parser).parse(
            default_resource_id, resources, attrs, raw.get("preprocessing", [])
        )
        AttrParser(path_parser).parse(
            default_resource_id, resources, attrs, raw["attributes"]
        )
        aligns = AlignParser.parse(raw.get("alignments", []))

        if "semantic_model" in raw:
            sm = SMParser.parse(raw["semantic_model"])
        else:
            sm = SemanticModel.get_default(attrs.attrs)

        return DRepr(resources, preprocessing, attrs.attrs, aligns, sm)

    @classmethod
    def dump(cls, drepr: "DRepr", simplify: bool = True, use_json_path: bool = False):
        version = "2"
        sm = OrderedDict()

        class_counter = defaultdict(int)
        class_ids: Dict[str, str] = {}
        for node in drepr.sm.nodes.values():
            if isinstance(node, ClassNode):
                class_counter[node.label] += 1
                class_ids[node.node_id] = f"{node.label}:{class_counter[node.label]}"
                sm[class_ids[node.node_id]] = OrderedDict(
                    [
                        ("properties", []),
                        ("static_properties", []),
                        ("inverse_static_properties", []),
                        ("links", []),
                    ]
                )

        for node in drepr.sm.nodes.values():
            if isinstance(node, DataNode):
                for edge in [
                    e for e in drepr.sm.edges.values() if e.target_id == node.node_id
                ]:
                    if node.data_type is not None:
                        prop = (edge.label, node.attr_id, node.data_type.get_rel_uri())
                    else:
                        prop = (edge.label, node.attr_id)
                    sm[class_ids[edge.source_id]]["properties"].append(prop)

            if isinstance(node, LiteralNode):
                for edge in [
                    e for e in drepr.sm.edges.values() if e.target_id == node.node_id
                ]:
                    if node.data_type is not None:
                        prop = (edge.label, node.value, node.data_type.get_rel_uri())
                    else:
                        prop = (edge.label, node.value)
                    sm[class_ids[edge.source_id]]["static_properties"].append(prop)
                for edge in [
                    e for e in drepr.sm.edges.values() if e.source_id == node.node_id
                ]:
                    if edge.target_id not in class_ids:
                        raise Exception(
                            "D-Repr YAML version 2 does not support link from literal node to non-class nodes"
                        )
                    sm[class_ids[edge.target_id]]["inverse_static_properties"].append(
                        (edge.label, node.value)
                    )

        for edge in drepr.sm.edges.values():
            if isinstance(drepr.sm.nodes[edge.source_id], ClassNode) and isinstance(
                drepr.sm.nodes[edge.target_id], ClassNode
            ):
                sm[class_ids[edge.source_id]]["links"].append(
                    (edge.label, class_ids[edge.target_id])
                )
            if edge.is_subject:
                v = drepr.sm.nodes[edge.target_id]
                assert isinstance(v, DataNode)
                sm[class_ids[edge.source_id]]["subject"] = v.attr_id

        sm["prefixes"] = drepr.sm.prefixes

        preprocessing: List[dict] = []
        for prepro in drepr.preprocessing:
            preprocessing.append(OrderedDict([("type", prepro.type.value)]))
            for k, v in asdict(prepro.value).items():
                preprocessing[-1][k] = v
            preprocessing[-1]["path"] = prepro.value.path.to_lang_format(use_json_path)

        return OrderedDict(
            [
                ("version", version),
                (
                    "resources",
                    OrderedDict(
                        [
                            (
                                res.id,
                                OrderedDict(
                                    [("type", res.type.value)]
                                    + (
                                        [(k, v) for k, v in asdict(res.prop).items()]
                                        if res.prop is not None
                                        else []
                                    )
                                ),
                            )
                            for res in drepr.resources
                        ]
                    ),
                ),
                ("preprocessing", preprocessing),
                (
                    "attributes",
                    OrderedDict(
                        [
                            (
                                attr.id,
                                OrderedDict(
                                    [
                                        ("resource_id", attr.resource_id),
                                        (
                                            "path",
                                            attr.path.to_lang_format(use_json_path),
                                        ),
                                        ("unique", attr.unique),
                                        ("sorted", attr.sorted.value),
                                        ("value_type", attr.value_type.value),
                                        ("missing_values", attr.missing_values),
                                    ]
                                ),
                            )
                            for attr in drepr.attrs
                        ]
                    ),
                ),
                (
                    "alignments",
                    [
                        (
                            OrderedDict(
                                [
                                    ("type", AlignmentType.Range.value),
                                    ("source", align.source),
                                    ("target", align.target),
                                    (
                                        "aligned_dims",
                                        [
                                            OrderedDict(
                                                [
                                                    ("source", step.source_idx),
                                                    ("target", step.target_idx),
                                                ]
                                            )
                                            for step in align.aligned_steps
                                        ],
                                    ),
                                ]
                            )
                            if isinstance(align, RangeAlignment)
                            else OrderedDict(
                                [
                                    ("type", AlignmentType.Value.value),
                                    ("source", align.source),
                                    ("target", align.target),
                                ]
                            )
                        )
                        for align in drepr.aligns
                    ],
                ),
                ("semantic_model", sm),
            ]
        )
