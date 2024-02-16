from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Optional

from rdflib import BNode, Graph, Literal, Namespace, URIRef

from drepr.models.drepr import DRepr
from drepr.models.sm import NodeId
from drepr.writers.base import StreamClassWriter


class RDFGraphWriter(StreamClassWriter):
    def __init__(self, prefixes: dict[str, str]):
        self.g: Graph = Graph()
        for prefix, ns in prefixes.items():
            self.g.bind(prefix, Namespace(ns))

        self.written_records: set[str] = set()
        self.subj: Optional[URIRef | BNode] = None
        self.buffer: list[tuple[URIRef, URIRef | BNode | Literal]] = []
        self.is_buffered: bool = False
        self.has_subj_data: bool = False

    # def begin_class(self, class_id: NodeId):
    #     self.desc.sm.nodes[class_id]

    # def end_class(self):
    #     pass

    def has_written_record(self, subj: str) -> bool:
        return subj in self.written_records

    def begin_record(self, subj: str, is_blank: bool, is_buffered: bool):
        if is_blank:
            self.subj = URIRef(subj)
        else:
            self.subj = BNode(subj)
        self.buffer = []
        self.is_buffered = is_buffered

    def end_record(self):
        if self.subj is None:
            # has been aborted
            return

        if len(self.buffer) > 0:
            for pred, obj in self.buffer:
                self.g.add((self.subj, pred, obj))
            self.buffer = []
        self.subj = None

    def abort_record(self):
        """Abort the record that is being written"""
        self.subj = None
        self.buffer = []

    def is_record_empty(self):
        return not self.has_subj_data

    def write_data_property(self, predicate_id: str, value: Any, dtype: Optional[str]):
        if self.is_buffered:
            self.buffer.append((URIRef(predicate_id), Literal(value, datatype=dtype)))
        else:
            assert self.subj is not None
            self.g.add(
                (self.subj, URIRef(predicate_id), Literal(value, datatype=dtype))
            )

    def write_object_property(
        self,
        predicate_id: str,
        object: str,
        is_subject_blank: bool,
        is_object_blank: bool,
        is_new_subj: bool,
    ):
        if is_object_blank:
            object = BNode(object)
        else:
            object = URIRef(object)
        if self.is_buffered:
            self.buffer.append((URIRef(predicate_id), object))
        else:
            assert self.subj is not None
            self.g.add((self.subj, URIRef(predicate_id), object))

    def write_to_string(self):
        return self.g.serialize(format="ttl")

    def write_to_file(self, filepath):
        self.g.serialize(filepath, format="ttl")
