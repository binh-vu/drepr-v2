from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import partial
from pathlib import Path

from codegen.models import AST, Memory, PredefinedFn, Program, Var, VarScope, expr, stmt
from typing_extensions import is_protocol

from drepr.models.prelude import Cardinality, DRepr, OutputFormat
from drepr.planning.class_map_plan import (
    BlankObject,
    BlankSubject,
    ClassesMapExecutionPlan,
    ClassMapPlan,
    ExternalIDSubject,
    InternalIDSubject,
)
from drepr.program_generation.alignment_fn import AlignmentFn, PathAccessor
from drepr.program_generation.program_space import VarSpace
from drepr.program_generation.writers import Writer
from drepr.utils.misc import assert_not_null, assert_true


@dataclass
class FileOutput:
    fpath: Path
    format: OutputFormat


@dataclass
class MemoryOutput:
    format: OutputFormat


Output = FileOutput | MemoryOutput


def gen_program(desc: DRepr, exec_plan: ClassesMapExecutionPlan, output: Output) -> AST:
    """Generate a program to convert the given D-REPR to a target format"""
    program = Program()
    mem = program.memory
    writer = Writer(desc, output.format)

    for res in desc.resources:
        program.root.import_(f"drepr.readers.prelude.read_source_{res.type.value}")
        program.root.import_(writer.get_writer_clspath())

    if isinstance(output, FileOutput):
        output_file = [Var.create(mem, "output_file", key=VarSpace.output_file())]
    else:
        output_file = []

    program.root.linebreak()
    main_fn = program.root.func(
        "main",
        [
            Var.create(mem, "resource", key=VarSpace.resource(res.id))
            for res in desc.resources
        ]
        + output_file,
    )

    for resource in desc.resources:
        var = Var.create(mem, "resource_data", key=VarSpace.resource_data(resource.id))
        main_fn.assign(
            mem,
            var,
            expr.ExprFuncCall(
                expr.ExprIdent(f"read_source_{resource.type.value}"),
                [expr.ExprVar(Var.deref(mem, key=VarSpace.resource(resource.id)))],
            ),
        )

    # define missing values of attributes
    main_fn.linebreak()
    for attr in desc.attrs:
        if len(attr.missing_values) > 0:
            main_fn.assign(
                mem,
                Var.create(
                    mem,
                    f"{attr.id}_missing_values",
                    key=VarSpace.attr_missing_values(attr.id),
                ),
                expr.ExprConstant(attr.missing_values),
            )

    # create a writer
    writer.create_writer(mem, main_fn)

    # for each class node, we generate a plan for each of them.
    for classplan in exec_plan.class_map_plans:
        main_fn.linebreak()
        main_fn.comment(f"Transform records of class {classplan.class_id}")

        varscope = main_fn.next_var_scope()

        # generate the code to execute the plan
        gen_classplan_executor(mem, main_fn, writer, desc, classplan)

        # claim the variables that aren't going to be used anymore
        for var in Var.find_by_scope(mem, varscope):
            var.delete(mem)

    main_fn.linebreak()
    # we write the output to the file
    if isinstance(output, FileOutput):
        assert len(output_file) > 0
        writer.write_to_file(mem, main_fn, expr.ExprVar(output_file[0]))
    else:
        content = Var.create(mem, "output", key=tuple())
        writer.write_to_string(mem, main_fn, content)
        main_fn.return_(expr.ExprVar(content))

    program.root.linebreak()
    program.root.if_(
        expr.ExprEqual(expr.ExprIdent("__name__"), expr.ExprConstant("__main__"))
    )(
        stmt.ImportStatement("sys"),
        stmt.SingleExprStatement(
            expr.ExprFuncCall(expr.ExprIdent("main"), [expr.ExprIdent("sys.argv[1:]")])
        ),
    )
    return program.root


def gen_classplan_executor(
    mem: Memory, parent_ast: AST, writer: Writer, desc: DRepr, classplan: ClassMapPlan
):
    """Generate the code to execute the given class plan.
    Below is the pseudo code:

    1. Iterate over the subject values
        1. If the subject is uri and it has missing values, if the uri is missing, we skip this
           record
        2. Begin record
        3. Iterate over target property & value
            1. If not target.can_have_missing_values:
                1. Iterate over objprop values:
                    1. Write property
            2. Else:
                1. If target edge is optional:
                    iterate over objprop values:
                        if objprop value is not missing:
                            write  property
                else:
                    (1) ----
                    has_record = False
                    iterate over objprop values:
                        if objprop value is not missing:
                            has_record = True
                            write property
                    if not has_record:
                        abort the record
                    ---- (2)
        4. End the record -- if the subject is blank node,
            and we do not write any data, we abort, otherwise, we commit
    """
    ast = PathAccessor().iterate_elements(
        mem, parent_ast, classplan.subject.attr, None, None
    )
    is_subj_blank = expr.ExprConstant(isinstance(classplan.subject, BlankSubject))
    can_class_missing = (
        any(
            not dprop.is_optional and dprop.can_target_missing
            for dprop in classplan.data_props
        )
        or any(
            not oprop.is_optional and not oprop.can_target_missing
            for oprop in classplan.object_props
        )
        or any(
            not oprop.is_optional and not oprop.can_target_missing
            for oprop in classplan.buffered_object_props
        )
    )
    is_buffered = can_class_missing

    get_subj_val = lambda: expr.ExprVar(
        Var.deref(
            mem,
            key=VarSpace.attr_value_dim(
                classplan.subject.attr.resource_id,
                classplan.subject.attr.id,
                len(classplan.subject.attr.path.steps) - 1,
            ),
        )
    )

    if (
        isinstance(classplan.subject, (InternalIDSubject, ExternalIDSubject))
        and len(classplan.subject.attr.missing_values) > 0
    ):
        # we know immediately that it's missing if the URI is missing

        # if subject is a single value, we can't use continue
        if ast.id == parent_ast.id:
            # same ast because of a single value, we can't use continue
            raise NotImplementedError()

        ast.if_(
            expr.ExprNegation(
                PredefinedFn.set_contains(
                    expr.ExprVar(
                        Var.deref(
                            mem,
                            key=VarSpace.attr_missing_values(classplan.subject.attr.id),
                        )
                    ),
                    get_subj_val(),
                )
            )
        )(stmt.ContinueStatement())

    writer.begin_record(mem, ast, get_subj_val(), is_subj_blank, is_buffered)

    for dataprop in classplan.data_props:
        ast.linebreak()
        ast.comment(f"Retrieve value of data property: {dataprop.attr.id}")

        get_dataprop_val = lambda: expr.ExprVar(
            Var.deref(
                mem,
                key=VarSpace.attr_value_dim(
                    dataprop.attr.resource_id,
                    dataprop.attr.id,
                    len(dataprop.attr.path.steps) - 1,
                ),
            )
        )
        is_dataprop_val_missing = lambda: PredefinedFn.set_contains(
            expr.ExprVar(
                Var.deref(
                    mem,
                    key=VarSpace.attr_missing_values(dataprop.attr.id),
                )
            ),
            get_dataprop_val(),
        )
        if not dataprop.can_target_missing:
            AlignmentFn(desc).align(mem, ast, dataprop.alignments)(
                lambda ast_l0: writer.write_data_property(
                    mem,
                    ast_l0,
                    expr.ExprConstant(dataprop.predicate),
                    get_dataprop_val(),
                    expr.ExprConstant(dataprop.datatype),
                )
            )
        else:
            if dataprop.is_optional:
                AlignmentFn(desc).align(mem, ast, dataprop.alignments)(
                    lambda ast00: ast00.if_(is_dataprop_val_missing())(
                        lambda ast01: writer.write_data_property(
                            mem,
                            ast01,
                            expr.ExprConstant(dataprop.predicate),
                            get_dataprop_val(),
                            expr.ExprConstant(dataprop.datatype),
                        )
                    )
                )
            else:
                if dataprop.alignments_cardinality.is_star_to_many():
                    has_dataprop_val = Var.create(
                        mem,
                        f"{dataprop.attr.id}_has_value_{len(dataprop.attr.path.steps) - 1}",
                        key=VarSpace.has_attr_value_dim(
                            dataprop.attr.resource_id,
                            dataprop.attr.id,
                            len(dataprop.attr.path.steps) - 1,
                        ),
                    )
                    ast.assign(mem, has_dataprop_val, expr.ExprConstant(False))
                    AlignmentFn(desc).align(mem, ast, dataprop.alignments)(
                        lambda ast00: ast00.if_(is_dataprop_val_missing())(
                            lambda ast01: ast01.assign(
                                mem, has_dataprop_val, expr.ExprConstant(True)
                            ),
                            lambda ast02: writer.write_data_property(
                                mem,
                                ast02,
                                expr.ExprConstant(dataprop.predicate),
                                get_dataprop_val(),
                                expr.ExprConstant(dataprop.datatype),
                            ),
                        )
                    )
                    ast.if_(expr.ExprNegation(expr.ExprVar(has_dataprop_val)))(
                        lambda ast00: (
                            assert_true(
                                is_buffered,
                                "We should only abort record if we are buffering",
                            )
                            and writer.abort_record(mem, ast00)
                        )
                    )
                else:
                    AlignmentFn(desc).align(mem, ast, dataprop.alignments)(
                        lambda ast00: ast00.if_(is_dataprop_val_missing())(
                            lambda ast01: (
                                assert_true(
                                    is_buffered,
                                    "We should only abort record if we are buffering",
                                )
                                and writer.abort_record(mem, ast01)
                            ),
                        ),
                        lambda ast10: ast10.else_()(
                            lambda ast11: writer.write_data_property(
                                mem,
                                ast11,
                                expr.ExprConstant(dataprop.predicate),
                                get_dataprop_val(),
                                expr.ExprConstant(dataprop.datatype),
                            ),
                        ),
                    )

    for objprop in classplan.object_props:
        ast.linebreak()
        ast.comment(f"Retrieve value of object property: {objprop.attr.id}")

        get_objprop_val = lambda: Var.deref(
            mem,
            key=VarSpace.attr_value_dim(
                objprop.attr.resource_id,
                objprop.attr.id,
                len(objprop.attr.path.steps) - 1,
            ),
        )

        if not objprop.can_target_missing:
            AlignmentFn(desc).align(mem, ast, objprop.alignments)(
                lambda inner_ast: writer.write_object_property(
                    mem,
                    inner_ast,
                    expr.ExprConstant(objprop.predicate),
                    expr.ExprVar(get_objprop_val()),
                    is_subj_blank,
                    expr.ExprConstant(isinstance(objprop, BlankObject)),
                    expr.ExprConstant(False),
                )
            )
        else:
            if objprop.is_optional:
                AlignmentFn(desc).align(mem, ast, objprop.alignments)(
                    lambda inner_ast: inner_ast.if_(
                        writer.has_written_record(
                            mem,
                            inner_ast,
                            expr.ExprVar(get_objprop_val()),
                        )
                    )(
                        lambda inner_ast_if: writer.write_object_property(
                            mem,
                            inner_ast_if,
                            expr.ExprConstant(objprop.predicate),
                            expr.ExprVar(get_objprop_val()),
                            is_subj_blank,
                            expr.ExprConstant(isinstance(objprop, BlankObject)),
                            expr.ExprConstant(False),
                        )
                    )
                )
            else:
                if objprop.alignments_cardinality.is_star_to_many():
                    has_objprop_val = Var.create(
                        mem,
                        f"{objprop.attr.id}_has_value_{len(objprop.attr.path.steps) - 1}",
                        key=VarSpace.has_attr_value_dim(
                            objprop.attr.resource_id,
                            objprop.attr.id,
                            len(objprop.attr.path.steps) - 1,
                        ),
                    )
                    ast.assign(mem, has_objprop_val, expr.ExprConstant(False))
                    AlignmentFn(desc).align(mem, ast, objprop.alignments)(
                        lambda ast_l0: ast_l0.if_(
                            writer.has_written_record(
                                mem,
                                ast_l0,
                                expr.ExprVar(get_objprop_val()),
                            )
                        )(
                            lambda ast_l1: ast_l1.assign(
                                mem, has_objprop_val, expr.ExprConstant(True)
                            ),
                            lambda ast_l1: writer.write_object_property(
                                mem,
                                ast_l1,
                                expr.ExprConstant(objprop.predicate),
                                expr.ExprVar(get_objprop_val()),
                                is_subj_blank,
                                expr.ExprConstant(isinstance(objprop, BlankObject)),
                                expr.ExprConstant(False),
                            ),
                        )
                    )
                    ast.if_(expr.ExprNegation(expr.ExprVar(has_objprop_val)))(
                        lambda ast_l0: (
                            assert_true(
                                is_buffered,
                                "We should only abort record if we are buffering",
                            )
                            and writer.abort_record(mem, ast_l0)
                        )
                    )
                else:
                    AlignmentFn(desc).align(mem, ast, objprop.alignments)(
                        lambda ast_l0: ast_l0.if_(
                            writer.has_written_record(
                                mem,
                                ast_l0,
                                expr.ExprVar(get_objprop_val()),
                            )
                        )(
                            lambda ast_l1: writer.write_object_property(
                                mem,
                                ast_l1,
                                expr.ExprConstant(objprop.predicate),
                                expr.ExprVar(get_objprop_val()),
                                is_subj_blank,
                                expr.ExprConstant(isinstance(objprop, BlankObject)),
                                expr.ExprConstant(False),
                            )
                        ),
                        lambda ast_l0: ast_l0.else_()(
                            lambda ast_l1: (
                                assert_true(
                                    is_buffered,
                                    "We should only abort record if we are buffering",
                                )
                                and writer.abort_record(mem, ast_l1)
                            )
                        ),
                    )

    assert len(classplan.buffered_object_props) == 0, "Not implemented yet"

    # we can end the record even if we abort it before. the end record code should handle this.
    ast.linebreak()

    if isinstance(classplan.subject, BlankSubject) and can_class_missing:
        ast.if_(writer.is_record_empty(mem, ast))(
            lambda ast00: writer.abort_record(mem, ast00)
        )
    else:
        writer.end_record(mem, ast)

    return ast
