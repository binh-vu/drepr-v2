from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import partial
from pathlib import Path
from typing import Callable

from codegen.models import AST, Memory, PredefinedFn, Program, Var, VarScope, expr, stmt
from codegen.models.program import ImportManager
from typing_extensions import is_protocol

from drepr.models.path import IndexExpr
from drepr.models.prelude import Cardinality, DRepr, OutputFormat
from drepr.models.preprocessing import PMap, Preprocessing, PreprocessingType
from drepr.planning.class_map_plan import (
    BlankObject,
    BlankSubject,
    ClassesMapExecutionPlan,
    ClassMapPlan,
    DataProp,
    ExternalIDSubject,
    IDObject,
    InternalIDSubject,
    ObjectProp,
    Subject,
)
from drepr.program_generation.alignment_fn import AlignmentFn, PathAccessor
from drepr.program_generation.predefined_fn import DReprPredefinedFn
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


def gen_program(
    desc: DRepr, exec_plan: ClassesMapExecutionPlan, output: Output, debuginfo: bool
) -> AST:
    """Generate a program to convert the given D-REPR to a target format"""
    program = Program()
    mem = program.memory
    writer = Writer(desc, output.format)

    func_args = [
        Var.create(mem, "resource", key=VarSpace.resource(res.id))
        for res in desc.resources
    ]
    if isinstance(output, FileOutput):
        output_file = Var.create(mem, "output_file", key=VarSpace.output_file())
        func_args.append(output_file)
    else:
        output_file = None

    program.root.linebreak()
    main_fn = program.root.func("main", func_args)

    for resource in desc.resources:
        var = Var.create(mem, "resource_data", key=VarSpace.resource_data(resource.id))
        main_fn.assign(
            mem,
            var,
            DReprPredefinedFn.read_source(
                program.import_manager,
                resource.type,
                Var.deref(mem, key=VarSpace.resource(resource.id)),
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

    # create transformation
    for preprocess in desc.preprocessing:
        gen_preprocess_executor(program, desc, main_fn, preprocess)

    # create a writer
    writer.create_writer(program.import_manager, mem, main_fn)

    # for each class node, we generate a plan for each of them.
    for classplan in exec_plan.class_map_plans:
        main_fn.linebreak()
        main_fn.comment(f"Transform records of class {classplan.class_id}")

        varscope = main_fn.next_var_scope()

        # generate the code to execute the plan
        gen_classplan_executor(
            program.import_manager, mem, main_fn, writer, desc, classplan, debuginfo
        )

        # claim the variables that aren't going to be used anymore
        for var in Var.find_by_scope(mem, varscope):
            var.delete(mem)

    main_fn.linebreak()
    # we write the output to the file
    if isinstance(output, FileOutput):
        assert output_file is not None
        writer.write_to_file(mem, main_fn, expr.ExprVar(output_file))
    else:
        content = Var.create(mem, "output", key=tuple())
        writer.write_to_string(mem, main_fn, content)
        main_fn.return_(expr.ExprVar(content))

    invok_main = expr.ExprFuncCall(
        expr.ExprIdent("main"), [expr.ExprIdent("*sys.argv[1:]")]
    )

    program.root.linebreak()
    program.root.if_(
        expr.ExprEqual(expr.ExprIdent("__name__"), expr.ExprConstant("__main__"))
    )(
        stmt.ImportStatement("sys"),
        stmt.LineBreak(),
        stmt.SingleExprStatement(
            expr.ExprFuncCall(expr.ExprIdent("print"), [invok_main])
            if isinstance(output, MemoryOutput)
            else invok_main
        ),
    )
    return program.root


def gen_classplan_executor(
    import_manager: ImportManager,
    mem: Memory,
    parent_ast: AST,
    writer: Writer,
    desc: DRepr,
    classplan: ClassMapPlan,
    debuginfo: bool,
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
    class_uri = expr.ExprConstant(
        desc.sm.get_abs_iri(desc.sm.get_class_node(classplan.class_id).label)
    )

    def on_missing_key(tree: AST):
        if parent_ast.has_statement_between_ast(stmt.ForLoopStatement, tree.id):
            tree(stmt.ContinueStatement())
        else:
            # same ast because of a single value, we can't use continue
            # however, we use pass as it's a single-level if/else -- the else part
            # will handle the instance generation if there is no missing value.
            tree(stmt.NoStatement())

    ast = PathAccessor(import_manager).iterate_elements(
        mem,
        parent_ast,
        classplan.subject.attr,
        None,
        None,
        validate_path=debuginfo,
        on_missing_key=(
            on_missing_key if classplan.subject.attr.path.has_optional_steps() else None
        ),
    )
    is_subj_blank = isinstance(classplan.subject, BlankSubject)
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

    if isinstance(classplan.subject, (InternalIDSubject, ExternalIDSubject)):
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
    else:
        # if this is a blank node, the subj_val is the entire index that leads to the last value
        _non_index_steps = [
            expr.ExprVar(
                Var.deref(
                    mem,
                    key=VarSpace.attr_index_dim(
                        classplan.subject.attr.resource_id,
                        classplan.subject.attr.id,
                        dim,
                    ),
                )
            )
            for dim, step in enumerate(classplan.subject.attr.path.steps)
            if not isinstance(step, IndexExpr)
        ]
        get_subj_val = lambda: (
            PredefinedFn.tuple(_non_index_steps)
            if len(_non_index_steps) > 1
            else _non_index_steps[0]
        )

    if (
        isinstance(classplan.subject, (InternalIDSubject, ExternalIDSubject))
        and len(classplan.subject.attr.missing_values) > 0
    ):
        # we know immediately that it's missing if the URI is missing

        if ast.id == parent_ast.id:
            # same ast because of a single value, we can't use continue
            # so we wrap it with if -- if not missing, continue to generate the instance
            ast = ast.if_(
                expr.ExprNegation(
                    PredefinedFn.set_contains(
                        expr.ExprVar(
                            Var.deref(
                                mem,
                                key=VarSpace.attr_missing_values(
                                    classplan.subject.attr.id
                                ),
                            )
                        ),
                        get_subj_val(),
                    )
                )
            )
        else:
            ast.if_(
                PredefinedFn.set_contains(
                    expr.ExprVar(
                        Var.deref(
                            mem,
                            key=VarSpace.attr_missing_values(classplan.subject.attr.id),
                        )
                    ),
                    get_subj_val(),
                )
            )(stmt.ContinueStatement())

    writer.begin_record(
        mem,
        ast,
        class_uri,
        get_subj_val(),
        expr.ExprConstant(is_subj_blank),
        is_buffered,
    )

    for dataprop in classplan.data_props:
        ast.linebreak()
        ast.comment(f"Retrieve value of data property: {dataprop.attr.id}")

        gen_classprop_body(
            import_manager,
            desc,
            mem,
            ast,
            writer,
            is_buffered,
            is_subj_blank,
            dataprop,
            debuginfo,
        )

    for objprop in classplan.object_props:
        ast.linebreak()
        ast.comment(f"Retrieve value of object property: {objprop.attr.id}")

        gen_classprop_body(
            import_manager,
            desc,
            mem,
            ast,
            writer,
            is_buffered,
            is_subj_blank,
            objprop,
            debuginfo,
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


def gen_classprop_body(
    import_manager: ImportManager,
    desc: DRepr,
    mem: Memory,
    ast: AST,
    writer: Writer,
    is_buffered: bool,
    is_subj_blank: bool,
    classprop: DataProp | ObjectProp,
    debuginfo: bool,
):
    attr = classprop.attr
    if isinstance(classprop, (DataProp, IDObject)):
        get_prop_val = lambda: expr.ExprVar(
            Var.deref(
                mem,
                key=VarSpace.attr_value_dim(
                    attr.resource_id,
                    attr.id,
                    len(attr.path.steps) - 1,
                ),
            )
        )
    else:
        assert isinstance(classprop, BlankObject)
        _non_index_steps = [
            expr.ExprVar(
                Var.deref(
                    mem,
                    key=VarSpace.attr_index_dim(
                        classprop.attr.resource_id,
                        classprop.attr.id,
                        dim,
                    ),
                )
            )
            for dim, step in enumerate(classprop.attr.path.steps)
            if not isinstance(step, IndexExpr)
        ]
        get_prop_val = lambda: (
            PredefinedFn.tuple(_non_index_steps)
            if len(_non_index_steps) > 1
            else _non_index_steps[0]
        )

    if isinstance(classprop, DataProp):
        if len(attr.missing_values) == 0:
            # leverage the fact that if True will be optimized away
            is_prop_val_not_missing = lambda: expr.ExprConstant(True)
        else:
            is_prop_val_not_missing = lambda: PredefinedFn.set_contains(
                expr.ExprNegation(
                    expr.ExprVar(
                        Var.deref(
                            mem,
                            key=VarSpace.attr_missing_values(attr.id),
                        )
                    )
                ),
                get_prop_val(),
            )
        write_fn = partial(
            writer.write_data_property, dtype=expr.ExprConstant(classprop.datatype)
        )
    else:
        assert isinstance(classprop, ObjectProp)
        is_prop_val_not_missing = lambda: writer.has_written_record(
            mem,
            get_prop_val(),
        )
        write_fn = partial(
            writer.write_object_property,
            is_subject_blank=expr.ExprConstant(is_subj_blank),
            is_object_blank=expr.ExprConstant(isinstance(classprop, BlankObject)),
            is_new_subj=expr.ExprConstant(False),
        )

    if not classprop.can_target_missing:
        AlignmentFn(desc, import_manager).align(
            mem, ast, classprop.alignments, debuginfo, None
        )(
            lambda ast_l0: write_fn(
                mem,
                ast_l0,
                expr.ExprConstant(classprop.predicate),
                get_prop_val(),
            )
        )
    else:
        if classprop.is_optional:
            AlignmentFn(desc, import_manager).align(
                mem,
                ast,
                classprop.alignments,
                debuginfo,
                # if the value is missing, we just ignore it.
                on_missing_key=lambda astxx: astxx(stmt.NoStatement()),
            )(
                lambda ast00: ast00.if_(is_prop_val_not_missing())(
                    lambda ast01: write_fn(
                        mem,
                        ast01,
                        expr.ExprConstant(classprop.predicate),
                        get_prop_val(),
                    )
                )
            )
        else:
            if classprop.alignments_cardinality.is_star_to_many():
                has_dataprop_val = Var.create(
                    mem,
                    f"{attr.id}_has_value_d{len(attr.path.steps) - 1}",
                    key=VarSpace.has_attr_value_dim(
                        attr.resource_id,
                        attr.id,
                        len(attr.path.steps) - 1,
                    ),
                )
                ast.assign(mem, has_dataprop_val, expr.ExprConstant(False))
                AlignmentFn(desc, import_manager).align(
                    mem,
                    ast,
                    classprop.alignments,
                    debuginfo,
                    lambda astxx: astxx(stmt.NoStatement()),
                )(
                    lambda ast00: ast00.if_(is_prop_val_not_missing())(
                        lambda ast01: ast01.assign(
                            mem, has_dataprop_val, expr.ExprConstant(True)
                        ),
                        lambda ast02: write_fn(
                            mem,
                            ast02,
                            expr.ExprConstant(classprop.predicate),
                            get_prop_val(),
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
                AlignmentFn(desc, import_manager).align(
                    mem,
                    ast,
                    classprop.alignments,
                    debuginfo,
                    on_missing_key=lambda astxx: assert_true(
                        is_buffered,
                        "We should only abort record if we are buffering",
                    )
                    and writer.abort_record(mem, astxx),
                )(
                    lambda ast00: ast00.if_(is_prop_val_not_missing())(
                        lambda ast01: write_fn(
                            mem,
                            ast01,
                            expr.ExprConstant(classprop.predicate),
                            get_prop_val(),
                        ),
                    ),
                    lambda ast10: ast10.else_()(
                        lambda ast11: (
                            assert_true(
                                is_buffered,
                                "We should only abort record if we are buffering",
                            )
                            and writer.abort_record(mem, ast11)
                        ),
                    ),
                )


def gen_preprocess_executor(
    program: Program, desc: DRepr, ast: AST, preprocessing: Preprocessing
) -> None:
    if preprocessing.type == PreprocessingType.pmap:
        value = preprocessing.value
        assert isinstance(value, PMap)

        # we don't support change_structure and output yet
        assert not value.change_structure and value.output is None

        raise NotImplementedError()

        program.root.linebreak()

        # define the transformation functionoc

        return

    raise NotImplementedError(preprocessing.type)
