from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, TypeAlias, cast

from drepr.models.prelude import (
    DREPR_URI,
    MISSING_VALUE_TYPE,
    Alignment,
    Attr,
    AttrId,
    Cardinality,
    ClassNode,
    DataNode,
    DRepr,
    EdgeId,
    LiteralNode,
    NodeId,
)
from drepr.planning.drepr_model_alignments import DReprModelAlignments
from drepr.planning.topological_sorting import topological_sorting


@dataclass
class ClassesMapExecutionPlan:
    # read_plans: list[ReadPlan]
    # write_plan: WritePlan
    class_map_plans: list[ClassMapPlan]

    @staticmethod
    def create(desc: DRepr):
        reversed_topo_orders = topological_sorting(desc.sm)
        alignments = DReprModelAlignments.create(desc)
        edges_optional = {e.edge_id: not e.is_required for e in desc.sm.edges.values()}
        class_map_plans = []

        # find subject attribute of each class
        class2subj = {}
        for class_id in reversed_topo_orders.topo_order:
            class2subj[class_id] = ClassMapPlan.find_subject(
                desc, class_id, class2subj, alignments
            )

        # generate plans
        for class_id in reversed_topo_orders.topo_order:
            class_map_plans.append(
                ClassMapPlan.create(
                    desc,
                    class_id,
                    class2subj,
                    alignments,
                    edges_optional,
                    reversed_topo_orders.removed_outgoing_edges,
                )
            )

        return ClassesMapExecutionPlan(class_map_plans)


@dataclass
class ClassMapPlan:
    class_id: str
    subject: Subject
    data_props: list[DataProp]
    literal_props: list[LiteralProp]
    object_props: list[ObjectProp]
    buffered_object_props: list[ObjectProp]

    @staticmethod
    def create(
        desc: DRepr,
        class_id: NodeId,
        class2subj: dict[NodeId, AttrId],
        inference: DReprModelAlignments,
        edges_optional: dict[int, bool],
        removed_edges: dict[int, bool],
    ):
        subj = class2subj[class_id]
        uri_dnode: Optional[DataNode] = None
        for e in desc.sm.iter_outgoing_edges(class_id):
            if e.get_abs_iri(desc.sm) == DREPR_URI:
                tmp = desc.sm.nodes[e.target_id]
                assert isinstance(tmp, DataNode)
                uri_dnode = tmp
                break

        # generate other properties
        literal_props = []
        data_props: list[DataProp] = []
        object_props = []
        buffered_object_props = []

        for e in desc.sm.iter_outgoing_edges(class_id):
            target = desc.sm.nodes[e.target_id]
            if isinstance(target, DataNode):
                attribute = desc.get_attr_by_id(target.attr_id)
                assert attribute is not None

                if e.get_abs_iri(desc.sm) != DREPR_URI:
                    data_props.append(
                        DataProp(
                            alignments=inference.get_alignments(subj, target.attr_id),
                            predicate=e.edge_id,
                            attr=attribute,
                            is_optional=edges_optional[e.edge_id],
                            missing_values=set(attribute.missing_values),
                        )
                    )
            elif isinstance(target, LiteralNode):
                literal_props.append(
                    LiteralProp(predicate=e.edge_id, value=target.value)
                )
            elif isinstance(target, ClassNode):
                attribute = desc.get_attr_by_id(class2subj[e.target_id])
                assert attribute is not None

                # a class node is optional if all of its properties are optional
                is_target_optional = all(
                    edges_optional[te.edge_id]
                    for te in desc.sm.iter_outgoing_edges(e.target_id)
                )
                alignments = inference.get_alignments(subj, attribute.id)

                if target.is_blank_node(desc.sm):
                    prop = BlankObject(
                        attr=attribute,
                        alignments_cardinality=inference.estimate_cardinality(
                            alignments
                        ),
                        alignments=alignments,
                        predicate_id=e.edge_id,
                        class_id=class_id,
                        is_optional=edges_optional[e.edge_id],
                        is_target_optional=is_target_optional,
                    )
                else:
                    prop = IDObject(
                        attr=attribute,
                        alignments_cardinality=inference.estimate_cardinality(
                            alignments
                        ),
                        alignments=alignments,
                        predicate_id=e.edge_id,
                        class_id=class_id,
                        is_optional=edges_optional[e.edge_id],
                        is_target_optional=is_target_optional,
                        missing_values=set(attribute.missing_values),
                    )

                if removed_edges[e.edge_id]:
                    buffered_object_props.append(prop)
                else:
                    object_props.append(prop)

        subj_attr = desc.get_attr_by_id(subj)
        assert subj_attr is not None

        if uri_dnode is None:
            subject = BlankSubject(
                attr=subj_attr,
            )
        else:
            # get missing values from the real subjects
            missing_values = set(subj_attr.missing_values)
            uri_dnode_inedge = desc.sm.get_edge_between_nodes(
                class_id, uri_dnode.node_id
            )
            assert uri_dnode_inedge is not None

            if uri_dnode.attr_id == subj:
                subject = InternalIDSubject(
                    attr=subj_attr,
                    is_optional=edges_optional[uri_dnode_inedge.edge_id],
                    missing_values=missing_values,
                )
            else:
                subject = ExternalIDSubject(
                    attr=subj_attr,
                    is_optional=edges_optional[uri_dnode_inedge.edge_id],
                    missing_values=missing_values,
                )

        return ClassMapPlan(
            class_id=class_id,
            subject=subject,
            data_props=data_props,
            literal_props=literal_props,
            object_props=object_props,
            buffered_object_props=buffered_object_props,
        )

    @staticmethod
    def find_subject(
        desc: DRepr,
        class_id: NodeId,
        class2subj: dict[NodeId, AttrId],
        desc_aligns: DReprModelAlignments,
    ):
        """
        Find the subject of the class among the attributes of the class.

        The subject has *-to-one relationship with other attributes.
        """
        # get data nodes, attributes, and the attribute that contains URIs of the class
        data_nodes: list[DataNode] = []
        attrs: list[AttrId] = []
        uri_attr: Optional[AttrId] = None

        for e in desc.sm.iter_outgoing_edges(class_id):
            target = desc.sm.nodes[e.target_id]

            if isinstance(target, DataNode):
                data_nodes.append(target)
                attrs.append(target.attr_id)

                if e.get_abs_iri(desc.sm) == DREPR_URI:
                    uri_attr = target.attr_id

        # if the subject attribute is provided, then, we will use it.
        subjs = []
        for u in data_nodes:
            e = desc.sm.get_edge_between_nodes(class_id, u.node_id)
            if e is not None and e.is_subject:
                subjs.append(u.attr_id)

        if len(subjs) == 0:
            if len(attrs) == 0:
                # there is a special case where the class has no data node, but only links to other classes
                # we need to get the subject from the other classes
                other_attrs = []
                for e in desc.sm.iter_outgoing_edges(class_id):
                    target = desc.sm.nodes[e.target_id]
                    if isinstance(target, ClassNode):
                        # we must have inferred the subject of the target class before (because of the topological sorting)
                        assert target.node_id in class2subj
                        target_subj = class2subj[target.node_id]
                        other_attrs.append(target_subj)
                subjs = desc_aligns.infer_subject(other_attrs)
            else:
                # invoke the inference to find the subject attribute
                subjs = desc_aligns.infer_subject(attrs)

        if len(subjs) == 0:
            raise Exception(
                "There is no subject attribute of class: {}. Users need to specify it explicitly",
                cast(ClassNode, desc.sm.nodes[class_id]).label,
            )

        return ClassMapPlan.select_subject(desc, class_id, subjs, attrs, uri_attr)

    @staticmethod
    def select_subject(
        desc: DRepr,
        class_id: NodeId,
        subjs: list[AttrId],
        attrs: list[AttrId],
        uri_attr: Optional[AttrId],
    ) -> AttrId:
        if uri_attr is not None and uri_attr in subjs:
            return uri_attr
        return subjs[0]


@dataclass
class BlankSubject:
    attr: Attr


@dataclass
class InternalIDSubject:
    attr: Attr
    is_optional: bool
    missing_values: set[MISSING_VALUE_TYPE]


@dataclass
class ExternalIDSubject:
    attr: Attr
    is_optional: bool
    missing_values: set[MISSING_VALUE_TYPE]


Subject: TypeAlias = BlankSubject | InternalIDSubject | ExternalIDSubject


@dataclass
class DataProp:
    alignments: list[Alignment]
    predicate: EdgeId
    attr: Attr
    is_optional: bool
    missing_values: set[MISSING_VALUE_TYPE]


@dataclass
class LiteralProp:
    predicate: EdgeId
    value: Any


@dataclass
class BlankObject:
    attr: Attr
    alignments: list[Alignment]
    alignments_cardinality: Cardinality
    predicate_id: EdgeId
    class_id: NodeId
    is_optional: bool
    # if the target class is optional
    is_target_optional: bool


@dataclass
class IDObject:
    attr: Attr
    alignments: list[Alignment]
    alignments_cardinality: Cardinality
    predicate_id: EdgeId
    class_id: NodeId
    is_optional: bool
    # if the target class is optional
    is_target_optional: bool
    missing_values: set[MISSING_VALUE_TYPE]


ObjectProp = BlankObject | IDObject
