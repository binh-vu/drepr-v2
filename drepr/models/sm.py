from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, TypeAlias, Union

from .attr import Attr, AttrId

DREPR_URI = "https://purl.org/drepr/1.0/uri"
NodeId: TypeAlias = str
EdgeId: TypeAlias = int


class DataType(Enum):
    xsd_decimal = "xsd:decimal"
    xsd_anyURI = "xsd:anyURI"
    xsd_gYear = "xsd:gYear"
    xsd_date = "xsd:date"
    xsd_dateTime = "xsd:dateTime"
    xsd_int = "xsd:int"
    xsd_string = "xsd:string"
    geo_wktLiteral = "geo:wktLiteral"


@dataclass
class ClassNode:
    node_id: NodeId
    label: str  # relative iri

    def get_abs_iri(self, sm: SemanticModel):
        """Get the absolute IRI of this node"""
        if sm.is_rel_iri(self.label):
            return sm.get_abs_iri(self.label)
        return self.label

    def get_rel_iri(self, sm: SemanticModel):
        if sm.is_rel_iri(self.label):
            return self.label
        return sm.get_rel_iri(self.label)

    def is_blank_node(self, sm: SemanticModel) -> bool:
        for e in sm.iter_outgoing_edges(self.node_id):
            if e.get_abs_iri(sm) == DREPR_URI:
                return False
        return True


@dataclass
class DataNode:
    node_id: NodeId
    attr_id: AttrId
    data_type: Optional[DataType] = None


@dataclass
class LiteralNode:
    node_id: NodeId
    # you should rely on data_type to get the type of value right. The parser may be wrong about it.
    value: Any
    data_type: Optional[DataType] = None


@dataclass
class Edge:
    edge_id: EdgeId
    source_id: NodeId
    target_id: NodeId
    label: str  # rel uri
    is_subject: bool = False
    is_required: bool = False

    def get_abs_iri(self, sm: SemanticModel):
        """Get the absolute IRI of the predicate"""
        if sm.is_rel_iri(self.label):
            return sm.get_abs_iri(self.label)
        return self.label

    def get_rel_iri(self, sm: SemanticModel):
        if sm.is_rel_iri(self.label):
            return self.label
        return sm.get_rel_iri(self.label)


Node = Union[LiteralNode, DataNode, ClassNode]


@dataclass
class SemanticModel:
    nodes: dict[NodeId, Node]
    edges: dict[EdgeId, Edge]
    prefixes: dict[str, str]

    @staticmethod
    def get_default(attrs: list[Attr]) -> SemanticModel:
        """
        Automatically generate a semantic model from a list of attributes.

        WARNING: the engine may not able to map data to this semantic model if the final output should be
        comprised of multiple tables.
        """
        prefixes = {"eg": "https://example.org/"}
        aids = {attr.id for attr in attrs}
        cid = None
        for i in range(len(attrs)):
            cid = f"c{i}"
            if cid not in aids:
                break
        assert cid is not None
        nodes: dict[str, Node] = {cid: ClassNode(cid, "eg:Record")}
        edges = {}
        for attr in attrs:
            nodes[attr.id] = DataNode(attr.id, attr.id, None)
            edge_id = len(edges)
            edges[edge_id] = Edge(edge_id, cid, attr.id, f"eg:{attr.id}")

        return SemanticModel(nodes, edges, prefixes)

    @staticmethod
    def get_default_prefixes() -> dict[str, str]:
        return {
            "drepr": "https://purl.org/drepr/1.0/",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "owl": "http://www.w3.org/2002/07/owl#",
        }

    @staticmethod
    def deserialize(raw: dict) -> SemanticModel:
        nodes = {}
        for nid, n in raw["nodes"].items():
            if n["type"] == "class_node":
                nodes[nid] = ClassNode(n["node_id"], n["label"])
            elif n["type"] == "data_node":
                nodes[nid] = DataNode(
                    n["node_id"],
                    n["attr_id"],
                    DataType(n["data_type"]) if n["data_type"] is not None else None,
                )
            elif n["type"] == "literal_node":
                nodes[nid] = LiteralNode(
                    n["node_id"],
                    n["value"],
                    DataType(n["data_type"]) if n["data_type"] is not None else None,
                )
            else:
                raise NotImplementedError()
        edges = {eid: Edge(**e) for eid, e in raw["edges"].items()}
        return SemanticModel(nodes, edges, raw["prefixes"])

    def remove_node(self, node_id: str):
        self.nodes.pop(node_id)
        removed_edges = []
        for eid, e in self.edges.items():
            if e.source_id == node_id or e.target_id == node_id:
                removed_edges.append(eid)
        for eid in removed_edges:
            self.edges.pop(eid)

    def class2dict(self, class_id: str) -> dict[str, Union[list[int], int]]:
        """
        Get a dictionary that contains information (predicates) about a given class
        """
        info = {}
        for eid, e in self.edges.items():
            if e.source_id != class_id:
                continue

            if e.label in info:
                if not isinstance(info[e.label], list):
                    info[e.label] = [info[e.label], eid]
                else:
                    info[e.label].append(eid)
            else:
                info[e.label] = eid
        return info

    def iter_class_nodes(self):
        for n in self.nodes.values():
            if isinstance(n, ClassNode):
                yield n

    def iter_outgoing_edges(self, node_id: str):
        for e in self.edges.values():
            if e.source_id == node_id:
                yield e

    def iter_incoming_edges(self, node_id: str):
        for e in self.edges.values():
            if e.target_id == node_id:
                yield e

    def iter_child_nodes(self, node_id: str):
        for e in self.edges.values():
            if e.source_id == node_id:
                yield self.nodes[e.source_id]

    def iter_parent_nodes(self, node_id: str):
        for e in self.edges.values():
            if e.target_id == node_id:
                yield self.nodes[e.target_id]

    def get_rel_iri(self, abs_iri: str) -> str:
        """Convert an absolute IRI to a relative IRI."""
        assert not self.is_rel_iri(abs_iri)
        for prefix, uri in self.prefixes.items():
            if abs_iri.startswith(uri):
                return f"{prefix}:{abs_iri.replace(uri, '')}"
        raise ValueError(
            "Cannot create relative IRI because there is no suitable prefix"
        )

    def get_abs_iri(self, rel_iri: str) -> str:
        """Convert a relative IRI to an absolute IRI."""
        assert self.is_rel_iri(rel_iri)
        prefix, val = rel_iri.split(":", 1)
        if prefix not in self.prefixes:
            raise ValueError(
                f"Cannot create absolute IRI because the prefix {prefix} does not exist"
            )
        return f"{self.prefixes[prefix]}{val}"

    def is_rel_iri(self, iri: str) -> bool:
        return iri.find("://") == -1 and iri.find(":") != -1

    def get_n_class_nodes(self) -> int:
        return sum(1 for _ in self.iter_class_nodes())

    def get_edge_between_nodes(self, source_id: str, target_id: str) -> Optional[Edge]:
        matched_edges = []
        for e in self.edges.values():
            if e.source_id == source_id and e.target_id == target_id:
                matched_edges.append(e)

        if len(matched_edges) == 0:
            return None
        elif len(matched_edges) == 1:
            return matched_edges[0]
        else:
            raise ValueError(
                f"Found multiple edges between {source_id} and {target_id}"
            )
