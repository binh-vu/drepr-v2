from __future__ import annotations

from typing import Optional

from codegen.models import AST, Memory, PredefinedFn, Var, expr

import drepr.models.path as path
from drepr.models.align import IdenticalAlign
from drepr.models.path import RangeExpr
from drepr.models.prelude import Alignment, Attr, DRepr, RangeAlignment
from drepr.program_generation.program_space import VarSpace


class AlignmentFn:

    def __init__(self, desc: DRepr):
        self.desc = desc

    def align(self, mem: Memory, ast: AST, aligns: list[Alignment]):
        for align in aligns:
            if isinstance(align, RangeAlignment):
                ast = self.align_by_range(mem, ast, align)
            elif isinstance(align, IdenticalAlign):
                # this is the alignment between the same attribute
                continue
            else:
                raise NotImplementedError(type(align))
        return ast

    def align_by_range(self, mem: Memory, ast: AST, align: RangeAlignment) -> AST:
        """Generate a piece of code that will generate variables (of target attr) to
        complete this alignment, if the alignment is one/many to one, then return ast is the same
        as we do not introduce nested statements. If the alignment is one/many to many, then
        we will need to have a for loop, hence, we have nested statements -> nested AST.
        """
        source = self.desc.get_attr_by_id(align.source)
        target = self.desc.get_attr_by_id(align.target)

        assert source is not None and target is not None
        to_aligned_dim = {
            step.target_idx: step.source_idx for step in align.aligned_steps
        }
        return PathAccessor().iterate_elements(
            mem, ast, target, aligned_attr=source, to_aligned_dim=to_aligned_dim
        )


class PathAccessor:
    """Generate code to access elements (indices & values) of an attribute"""

    def iterate_elements(
        self,
        mem: Memory,
        ast: AST,
        attr: Attr,
        aligned_attr: Optional[Attr] = None,
        to_aligned_dim: Optional[dict[int, int]] = None,
    ):
        ast = ast.update_recursively(
            fn=lambda ast, dim: self.next_dimensions(
                mem, ast, attr, dim, aligned_attr, to_aligned_dim
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
    ):
        """Generate code to access elements of dimensions of attr started at dim.
        Return the next ast, remaining dimension index, and whether it has stopped.
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

            ast.assign(
                mem,
                c1,
                PredefinedFn.item_getter(
                    expr.ExprVar(collection), expr.ExprConstant(step.val)
                ),
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

            if to_aligned_dim is not None:
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
                    ast.assign(mem, end_var, PredefinedFn.len(expr.ExprVar(collection)))
                else:
                    if isinstance(step.end, path.Expr):
                        # I don't know about recursive path expression yet.
                        raise Exception(
                            f"Recursive path expression is not supported yet. Please raise a ticket to notify us for future support! Found: {step.end}"
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
