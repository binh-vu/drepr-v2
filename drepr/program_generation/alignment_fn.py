from __future__ import annotations

from typing import Any, Callable, Literal, Optional

from codegen.models import AST, Memory, PredefinedFn, Var, expr, stmt
from codegen.models.program import ImportManager

import drepr.models.path as path
from drepr.models.align import IdenticalAlign
from drepr.models.path import RangeExpr
from drepr.models.prelude import Alignment, Attr, DRepr, RangeAlignment
from drepr.program_generation.predefined_fn import DReprPredefinedFn
from drepr.program_generation.program_space import VarSpace
from drepr.utils.misc import assert_not_null


class AlignmentFn:

    def __init__(
        self,
        desc: DRepr,
        import_manager: ImportManager,
    ):
        self.desc = desc
        self.import_manager = import_manager

    def align(
        self,
        mem: Memory,
        ast: AST,
        aligns: list[Alignment],
        validate_path: bool,
        on_missing_key: Optional[Callable[[AST], Any]],
    ):
        for align in aligns:
            if isinstance(align, RangeAlignment):
                ast = self.align_by_range(
                    mem, ast, align, validate_path, on_missing_key
                )
            elif isinstance(align, IdenticalAlign):
                # this is the alignment between the same attribute
                continue
            else:
                raise NotImplementedError(type(align))
        return ast

    def align_by_range(
        self,
        mem: Memory,
        ast: AST,
        align: RangeAlignment,
        validate_path: bool,
        on_missing_key: Optional[Callable[[AST], Any]],
    ) -> AST:
        """Generate a piece of code that will generate variables (of target attr) to
        complete this alignment, if the alignment is one/many to one, then return ast is the same
        as we do not introduce nested statements. If the alignment is one/many to many, then
        we will need to have a for loop, hence, we have nested statements -> nested AST.
        """
        source = self.desc.get_attr_by_id(align.source)
        target = self.desc.get_attr_by_id(align.target)

        to_aligned_dim = {
            step.target_idx: step.source_idx for step in align.aligned_steps
        }
        return PathAccessor(self.import_manager).iterate_elements(
            mem,
            ast,
            target,
            aligned_attr=source,
            to_aligned_dim=to_aligned_dim,
            validate_path=validate_path,
            on_missing_key=on_missing_key,
        )


class PathAccessor:
    """Generate code to access elements (indices & values) of an attribute"""

    def __init__(self, import_manager: ImportManager):
        self.import_manager = import_manager

    def iterate_elements(
        self,
        mem: Memory,
        ast: AST,
        attr: Attr,
        aligned_attr: Optional[Attr] = None,
        to_aligned_dim: Optional[dict[int, int]] = None,
        validate_path: bool = False,
        on_missing_key: Optional[Callable[[AST], Any]] = None,
    ):
        ast = ast.update_recursively(
            fn=lambda ast, dim: self.next_dimensions(
                mem,
                ast,
                attr,
                dim,
                aligned_attr,
                to_aligned_dim,
                validate_path,
                on_missing_key,
            ),
            context=0,
        )
        return ast

    def next_dimensions(
        self,
        mem: Memory,
        ast: AST,
        attr: Attr,
        dim: int,
        aligned_attr: Optional[Attr],
        to_aligned_dim: Optional[dict[int, int]],
        validate_path: bool,
        on_missing_key: Optional[Callable[[AST], Any]] = None,
    ):
        """Generate code to access elements of dimensions of attr started at dim.
        Return the next ast, remaining dimension index, and whether it has stopped.

        Args:
            mem: memory to store variables
            ast: current ast
            attr: attribute
            dim: starting dimension
            aligned_attr:
            to_aligned_dim:
            validate_path: whether to generate code to check if the key of the dimension exists. If the attribute
                is annotated with `missing_path = True`, then setting this does not have any effect.
            type_check: whether to generate code to check if the type of the elements is correct (e.g., accessing number expecting a list or map)
            on_missing_key: a function that will be called when the key does not exist. If it is None, then we will raise an exception.
        """
        if dim >= len(attr.path.steps):
            return ast, dim, True

        if dim == 0:
            collection = Var.deref(mem, key=VarSpace.resource_data(attr.resource_id))
        else:
            collection = Var.deref(
                mem,
                key=VarSpace.attr_value_dim(attr.resource_id, attr.id, dim - 1),
            )

        # index expr does not need nested ast.
        step = attr.path.steps[dim]
        while isinstance(step, path.IndexExpr) and dim < len(attr.path.steps):
            # we do not need nested loop for index expression as we can just directly access the value
            c1 = Var.create(
                mem,
                name=f"{attr.id}_value_{dim}",
                key=VarSpace.attr_value_dim(attr.resource_id, attr.id, dim),
            )
            if isinstance(step.val, path.Expr):
                # I don't know about recursive path expression yet.
                raise Exception(
                    f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.val}"
                )

            if validate_path and not attr.path.is_step_optional(dim):
                handle_missing_key = "safe"
            elif attr.path.is_step_optional(dim):
                assert on_missing_key is not None
                handle_missing_key = on_missing_key
            else:
                handle_missing_key = "no_missing_key"

            ast = self.access_key(
                mem,
                ast,
                attr,
                expr.ExprVar(collection),
                expr.ExprConstant(step.val),
                c1,
                dim,
                handle_missing_key,
            )

            collection = c1
            dim += 1
            if dim == len(attr.path.steps):
                # we have reached the end of the path
                return ast, dim, True
            step = attr.path.steps[dim]

        assert not isinstance(step, path.IndexExpr), (attr, step, dim)

        # other exprs require nested statement (for loop)

        if isinstance(step, path.RangeExpr):
            itemindex = Var.create(
                mem,
                name=f"{attr.id}_index_{dim}",
                key=VarSpace.attr_index_dim(attr.resource_id, attr.id, dim),
            )
            itemvalue = Var.create(
                mem,
                name=f"{attr.id}_value_{dim}",
                key=VarSpace.attr_value_dim(attr.resource_id, attr.id, dim),
            )

            if to_aligned_dim is not None and dim in to_aligned_dim:
                # this attribute has been aligned with other attribute and
                # the dimension is bound to the previously set dimension (of a subject)
                # so we need to copy the value
                assert aligned_attr is not None
                aligned_dim = to_aligned_dim[dim]
                aligned_dim_index = Var.deref(
                    mem,
                    key=VarSpace.attr_index_dim(
                        aligned_attr.resource_id, aligned_attr.id, aligned_dim
                    ),
                )

                if step == aligned_attr.path.steps[aligned_dim]:
                    # now if the start, end, and step between the two attrs are the same, we just copy the value
                    # otherwise, we need to readjust the index
                    ast.assign(mem, itemindex, expr.ExprVar(aligned_dim_index))
                else:
                    # recalculate the index
                    raise NotImplementedError()

                if validate_path:
                    invok_item_getter = DReprPredefinedFn.safe_item_getter(
                        self.import_manager,
                        expr.ExprVar(collection),
                        expr.ExprVar(itemindex),
                        expr.ExprConstant(
                            f"Encounter error while accessing element of attribute {attr.id} via alignment at "
                            + f"dimension = {dim} - full path = {attr.path.to_lang_format()}"
                        ),
                    )
                else:
                    invok_item_getter = PredefinedFn.item_getter(
                        expr.ExprVar(collection), expr.ExprVar(itemindex)
                    )

                ast.assign(mem, itemvalue, invok_item_getter)
            else:
                # the dimension is not bound, we are going to generate multiple values
                # using a for loop
                start_var = Var.create(mem, f"start__local_ast_{ast.id}")
                if isinstance(step.start, path.Expr):
                    # I don't know about recursive path expression yet.
                    raise Exception(
                        f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.start}"
                    )
                ast.assign(mem, start_var, expr.ExprConstant(step.start))

                end_var = Var.create(mem, f"end__local_ast_{ast.id}")
                if step.end is None:
                    if validate_path:
                        invok_len = DReprPredefinedFn.safe_len(
                            self.import_manager,
                            expr.ExprVar(collection),
                            expr.ExprConstant(
                                f"Encounter error while computing number of elements of attribute {attr.id} at "
                                + f"dimension = {dim} - full path = {attr.path.to_lang_format()}"
                            ),
                        )
                    else:
                        invok_len = PredefinedFn.len(expr.ExprVar(collection))
                    ast.assign(mem, end_var, invok_len)
                else:
                    if isinstance(step.end, path.Expr):
                        # I don't know about recursive path expression yet.
                        raise Exception(
                            f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.end}"
                        )

                    if validate_path:
                        invok_len = DReprPredefinedFn.safe_len(
                            self.import_manager,
                            expr.ExprVar(collection),
                            expr.ExprConstant(
                                f"Encounter error while computing number of elements of attribute {attr.id} at "
                                + f"dimension = {dim} - full path = {attr.path.to_lang_format()}"
                            ),
                        )

                        ast.if_(
                            expr.ExprLessThanOrEqual(
                                invok_len, expr.ExprConstant(step.end)
                            )
                        )(
                            stmt.ExceptionStatement(
                                PredefinedFn.base_error(
                                    f"Trying to select out-of-bound elements of attribute {attr.id} at dimension = {dim} - full path = {attr.path.to_lang_format()}"
                                )
                            )
                        )

                    ast.assign(mem, end_var, expr.ExprConstant(step.end))

                if isinstance(step.step, path.Expr):
                    # I don't know about recursive path expression yet.
                    raise Exception(
                        f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.step}"
                    )
                elif step.step != 1:
                    step_var = Var.create(mem, f"step__local_ast_{ast.id}")
                    ast.assign(mem, step_var, expr.ExprConstant(step.step))
                    expr_step_var = expr.ExprVar(step_var)
                else:
                    expr_step_var = None

                ast = ast.for_loop(
                    item=itemindex,
                    iter=PredefinedFn.range(
                        expr.ExprVar(start_var), expr.ExprVar(end_var), expr_step_var
                    ),
                )

                ast.assign(
                    mem,
                    itemvalue,
                    PredefinedFn.item_getter(
                        expr.ExprVar(collection), expr.ExprVar(itemindex)
                    ),
                )
            return (
                ast,
                dim + 1,
                False,
            )

        raise NotImplementedError(step)

    def access_key(
        self,
        mem: Memory,
        ast: AST,
        attr: Attr,
        collection: expr.Expr,
        key: expr.ExprConstant,
        result: Var,
        dim: int,
        handle_missing_key: Literal["safe", "no_missing_key"] | Callable[[AST], None],
    ):
        if handle_missing_key == "no_missing_key":
            ast.assign(mem, result, PredefinedFn.item_getter(collection, key))
            return ast

        if handle_missing_key == "safe":
            ast.assign(
                mem,
                result,
                DReprPredefinedFn.safe_item_getter(
                    self.import_manager,
                    collection,
                    key,
                    expr.ExprConstant(
                        f"While traveling elements of attribute {attr.id}, encounter key error: "
                        + f"key {key.constant} does not exist (key position = {dim} - full path = {attr.path.to_lang_format()})"
                    ),
                ),
            )
            return ast

        ast.if_(expr.ExprNegation(PredefinedFn.has_item(collection, key)))(
            # if the key does not exist, we call the function to handle it
            handle_missing_key
        )
        inner_ast = ast.else_()
        inner_ast.assign(mem, result, PredefinedFn.item_getter(collection, key))
        return inner_ast
