from __future__ import annotations

from codegen.models import AST, Memory, Var, expr

from drepr.models.prelude import DRepr, OutputFormat
from drepr.program_generation.program_space import VarSpace
from drepr.utils.misc import assert_not_null


class Writer:
    def __init__(self, desc: DRepr, format: OutputFormat):
        self.desc = desc
        self.format = format

    def get_writer_clspath(self):
        if self.format == OutputFormat.TTL:
            return f"drepr.writers.rdfgraph_writer.RDFGraphWriter"
        else:
            raise NotImplementedError()

    def create_writer(self, mem: Memory, ast: AST):
        writer_clsname = self.get_writer_clspath().rsplit(".", 1)[-1]
        ast.assign(
            mem,
            Var.create(mem, "writer", key=VarSpace.writer()),
            expr.ExprFuncCall(
                expr.ExprIdent(writer_clsname),
                [expr.ExprConstant(self.desc.sm.prefixes)],
            ),
        )

    def has_written_record(self, mem: Memory, prog: AST, subj: expr.Expr):
        return expr.ExprMethodCall(
            expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
            "has_written_record",
            [subj],
        )

    def begin_class(self, mem: Memory, prog: AST, class_uri: str):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "begin_class",
                [expr.ExprConstant(class_uri)],
            )
        )

    def begin_record(
        self,
        mem: Memory,
        prog: AST,
        subj: expr.Expr,
        is_blank: expr.Expr,
        is_buffered: bool,
    ):
        """whether to bufferef the records because some properties are mandatory."""
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "begin_record",
                [subj, is_blank, expr.ExprConstant(is_buffered)],
            )
        )

    def end_record(self, mem: Memory, prog: AST):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())), "end_record", []
            )
        )

    def abort_record(self, mem: Memory, prog: AST):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())), "abort_record", []
            )
        )

    def is_record_empty(self, mem: Memory, prog: AST):
        return expr.ExprMethodCall(
            expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
            "is_record_empty",
            [],
        )

    def begin_partial_buffering_record(
        self,
        mem: Memory,
        prog: AST,
    ):
        raise NotImplementedError()

    def write_data_property(
        self,
        mem: Memory,
        prog: AST,
        predicate_id: expr.Expr,
        value: expr.ExprVar,
        dtype: expr.ExprConstant,
    ):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "write_data_property",
                [predicate_id, value, dtype],
            )
        )

    def write_object_property(
        self,
        mem: Memory,
        prog: AST,
        predicate_id: expr.Expr,
        object: expr.Expr,
        is_subject_blank: expr.Expr,
        is_object_blank: expr.Expr,
        is_new_subj: expr.Expr,
    ):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "write_object_property",
                [predicate_id, object, is_subject_blank, is_object_blank, is_new_subj],
            )
        )

    def buffer_object_property(
        self,
        target_cls: str,
        predicate_id: str,
        object: str,
        is_object_blank: bool,
    ):
        raise NotImplementedError()

    def write_to_file(self, mem: Memory, prog: AST, file_path: expr.Expr):
        prog.expr(
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "write_to_file",
                [file_path],
            )
        )

    def write_to_string(self, mem: Memory, prog: AST, content: Var):
        prog.assign(
            mem,
            content,
            expr.ExprMethodCall(
                expr.ExprVar(Var.deref(mem, key=VarSpace.writer())),
                "write_to_string",
                [],
            ),
        )
