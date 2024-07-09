from __future__ import annotations

from typing import Any, Optional
from io import StringIO
from drepr.models.sm import DREPR_URI
from drepr.writers.base import StreamClassWriter
from rdflib import RDF, BNode, Graph, Literal, Namespace, URIRef
# from rdflib.namespace import NamespaceManager
from drepr.writers.prefix_index import NamespaceManager

SubjVal = str | tuple | int | bool


class RDFGraphWriter(StreamClassWriter):
    def __init__(self, prefixes: dict[str, str], normalize_uri: bool = False):
        self.write_stream = StringIO()
        if normalize_uri:
            # self.namespace_manager = NamespaceManager(Graph())
            # for prefix, ns in prefixes.items():
            #     self.namespace_manager.bind(prefix, Namespace(ns), override=False)
            self.namespace_manager = NamespaceManager.from_prefix2ns(prefixes)
        else:
            self.namespace_manager = None
        self.written_records: dict[SubjVal, BNode | URIRef] = {}
        self.origin_subj: SubjVal = ""
        self.subj: Optional[URIRef | BNode] = None
        self.buffer: list[tuple[URIRef, URIRef | BNode | Literal]] = []
        self.is_buffered: bool = False
        # whether the current subject has any data or not
        # if the subject has URI, then it has data
        self.subj_has_data: bool = False

    def has_written_record(self, subj: SubjVal) -> bool:
        return subj in self.written_records

    def begin_record(
        self, class_uri: str, subj: SubjVal, is_blank: bool, is_buffered: bool
    ):
        self.origin_subj = subj
        if is_blank:
            if subj in self.written_records:
                self.subj = self.written_records[subj]
                self.subj_has_data = True
            else:
                self.subj = BNode()
                self.subj_has_data = False
        else:
            # subj will be a string for URIRef
            self.subj = URIRef(subj)  # type: ignore
            self.subj_has_data = True

        if is_buffered:
            self.buffer = [(RDF.type, URIRef(class_uri))]
        else:
            self.write_triple(self.subj, RDF.type, URIRef(class_uri))
        self.is_buffered = is_buffered
        self.subj_has_data = False

    def end_record(self):
        if self.subj is None:
            # has been aborted
            return

        if len(self.buffer) > 0:
            for pred, obj in self.buffer:
                self.write_pred_obj(pred, obj)
            self.buffer = []
        self.write_stream.write("\t.\n")
        self.written_records[self.origin_subj] = self.subj
        self.subj = None
        self.subj_has_data = False

    def abort_record(self):
        """Abort the record that is being written"""
        self.subj = None
        self.subj_has_data = False
        self.buffer = []

    def is_record_empty(self) -> bool:
        return not self.subj_has_data

    def write_data_property(self, predicate_id: str, value: Any, dtype: Optional[str]):
        if self.subj is None:
            return
        if dtype == DREPR_URI:
            value = URIRef(value)
        else:
            # to handle a bug in RDFlib that does not serialize integer properly.
            if (
                dtype == "http://www.w3.org/2001/XMLSchema#integer"
                or dtype == "http://www.w3.org/2001/XMLSchema#long"
                or dtype == "http://www.w3.org/2001/XMLSchema#int"
            ):
                value = int(float(value))
            value = Literal(value, datatype=dtype)

        self.subj_has_data = True
        if self.is_buffered:
            self.buffer.append((URIRef(predicate_id), value))
        else:
            assert self.subj is not None
            self.write_pred_obj(URIRef(predicate_id), value)

    def write_object_property(
        self,
        predicate_id: str,
        object: SubjVal,
        is_subject_blank: bool,
        is_object_blank: bool,
        is_new_subj: bool,
    ):
        if self.subj is None:
            return
        object = self.written_records[object]
        self.subj_has_data = True
        if self.is_buffered:
            self.buffer.append((URIRef(predicate_id), object))
        else:
            assert self.subj is not None
            self.write_pred_obj(URIRef(predicate_id), object)

    def write_to_string(self):
        return self.write_stream.getvalue()

    def write_to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.write_stream.getvalue())

    def write_triple(self, subj: URIRef | BNode, pred, obj):
        self.write_stream.write(subj.n3(self.namespace_manager))
        self.write_stream.write(" ")
        self.write_stream.write(pred.n3(self.namespace_manager))
        self.write_stream.write(" ")
        self.write_stream.write(obj.n3(self.namespace_manager))
        self.write_stream.write(" ;\n")

    def write_pred_obj(self, pred, obj):
        self.write_stream.write("\t")
        self.write_stream.write(pred.n3(self.namespace_manager))
        self.write_stream.write(" ")
        self.write_stream.write(obj.n3(self.namespace_manager))
        self.write_stream.write(" ;\n")