from __future__ import annotations

from dataclasses import dataclass
from functools import partial

from codegen.models import AST, Memory, PredefinedFn, Var, expr

import drepr.models.path as path
from drepr.models.prelude import DRepr
from drepr.planning.class_map_plan import ClassesMapExecutionPlan, ClassMapPlan
from drepr.program_generation.program_space import VarSpace


def gen_program(desc: DRepr, exec_plan: ClassesMapExecutionPlan) -> AST:
    """Generate a program to convert the given D-REPR to a target format"""
    root = AST.root()
    mem = Memory()

    for res in desc.resources:
        root.import_(f"drepr.readers.prelude.read_source_{res.type.value}")

    root.linebreak()
    main_fn = root.func(
        "main",
        [
            Var.create(mem, "resource", key=VarSpace.resource(res.id))
            for res in desc.resources
        ],
    )

    for resource in desc.resources:
        var = Var.create(mem, "resource_data", key=VarSpace.resource_data(resource.id))
        main_fn.assign(
            var,
            expr.ExprFuncCall(
                expr.ExprIdent(f"read_source_{resource.type.value}"),
                [expr.ExprVar(Var.deref(mem, key=VarSpace.resource(resource.id)))],
            ),
        )

    # for each class node, we generate a plan for each of them.
    for classplan in exec_plan.class_map_plans:
        main_fn.linebreak()
        gen_classplan_executor(mem, main_fn, desc, classplan)

    return root


@dataclass
class ExtractSubjectValueArgs:
    classplan: ClassMapPlan
    dim: int


@dataclass
class ExtractDataPropValueArgs:
    classplan: ClassMapPlan
    index: int


def gen_classplan_executor(mem: Memory, ast: AST, desc: DRepr, classplan: ClassMapPlan):
    inner_subj_val_ast = ast.update_recursively(
        fn=partial(extract_subject_value, mem),
        context=ExtractSubjectValueArgs(classplan, 0),
    )

    # for each other attribute, we generate a plan for each of them.
    for dataprop in classplan.data_props:
        extract_data_prop_value(mem, inner_subj_val_ast)


def extract_subject_value(mem: Memory, ast: AST, context: ExtractSubjectValueArgs):
    """Geerate an nested loop that get a subject item index and value"""

    subj_attr = context.classplan.subject.attr
    dim = context.dim

    if dim >= len(subj_attr.path.steps):
        # stopping condition, we have reached the end of the path
        return ast, context, True

    if dim == 0:
        collection = Var.deref(mem, key=VarSpace.resource_data(subj_attr.resource_id))
    else:
        collection = Var.deref(
            mem,
            key=VarSpace.attr_value_dim(subj_attr.resource_id, subj_attr.id, dim - 1),
        )

    step = subj_attr.path.steps[dim]
    while isinstance(step, path.IndexExpr) and dim < len(subj_attr.path.steps):
        # we do not need nested loop for index expression as we can just directly access the value
        c1 = Var.create(
            mem,
            name=f"{subj_attr.id}_value_{dim}",
            key=VarSpace.attr_value_dim(subj_attr.resource_id, subj_attr.id, dim),
        )
        if isinstance(step.val, path.Expr):
            # I don't know about recursive path expression yet.
            raise Exception(
                f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.val}"
            )

        ast.assign(
            c1,
            PredefinedFn.item_getter(
                expr.ExprVar(collection), expr.ExprConstant(step.val)
            ),
        )

        collection = c1
        dim += 1
        if dim == len(subj_attr.path.steps):
            # we have reached the end of the path
            return ast, ExtractSubjectValueArgs(context.classplan, dim), True
        step = subj_attr.path.steps[dim]

    assert not isinstance(step, path.IndexExpr), (subj_attr, step, dim)

    if isinstance(step, path.RangeExpr):
        start_var = Var.create(mem, f"start__local_ast_{ast.id}")
        if isinstance(step.start, path.Expr):
            # I don't know about recursive path expression yet.
            raise Exception(
                f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.start}"
            )
        ast.assign(start_var, expr.ExprConstant(step.start))

        end_var = Var.create(mem, f"end__local_ast_{ast.id}")
        if step.end is None:
            ast.assign(end_var, PredefinedFn.len(expr.ExprVar(collection)))
        else:
            if isinstance(step.end, path.Expr):
                # I don't know about recursive path expression yet.
                raise Exception(
                    f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.end}"
                )
            ast.assign(end_var, expr.ExprConstant(step.end))

        if isinstance(step.step, path.Expr):
            # I don't know about recursive path expression yet.
            raise Exception(
                f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.step}"
            )
        elif step.step != 1:
            step_var = Var.create(mem, f"step__local_ast_{ast.id}")
            ast.assign(step_var, expr.ExprConstant(step.step))
            expr_step_var = expr.ExprVar(step_var)
        else:
            expr_step_var = None

        itemindex = Var.create(
            mem,
            name=f"{subj_attr.id}_index_{dim}",
            key=VarSpace.attr_index_dim(subj_attr.resource_id, subj_attr.id, dim),
        )
        inner_loop_ast = ast.for_loop(
            item=itemindex,
            iter=PredefinedFn.range(
                expr.ExprVar(start_var), expr.ExprVar(end_var), expr_step_var
            ),
        )
        itemvalue = Var.create(
            mem,
            name=f"{subj_attr.id}_value_{dim}",
            key=VarSpace.attr_value_dim(subj_attr.resource_id, subj_attr.id, dim),
        )
        inner_loop_ast.assign(
            itemvalue,
            PredefinedFn.item_getter(expr.ExprVar(collection), expr.ExprVar(itemindex)),
        )

        return (
            inner_loop_ast,
            ExtractSubjectValueArgs(context.classplan, dim + 1),
            False,
        )

    raise NotImplementedError(step)


def extract_data_prop_value(mem: Memory, ast: AST, context: ExtractDataPropValueArgs):
    if context.index >= len(context.classplan.data_props):
        return ast, context, False

    data_prop = context.classplan.data_props[context.index]

    # convert subject index into attr index
