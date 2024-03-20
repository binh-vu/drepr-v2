from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from codegen.models import (
    AST,
    Program,
    Var,
    expr,
)

from drepr.models.attr import Attr, Sorted, ValueType
from drepr.models.drepr import DRepr
from drepr.models.preprocessing import Context, PMap, PreprocessingType
from drepr.program_generation.alignment_fn import PathAccessor
from drepr.program_generation.predefined_fn import DReprPredefinedFn
from drepr.program_generation.program_space import VarSpace
from drepr.utils.udf import SourceTree, UDFParsedResult, UDFParser

PreprocessingId = int


@dataclass
class NormedUserDefinedFn:
    name: str
    fnvar: Var
    udf: UDFParsedResult
    use_context: bool


class GenPreprocessing:
    """Generate preprocessing code for the given D-REPR."""

    def __init__(self, program: Program, desc: DRepr, call_preproc_ast: AST):
        self.program = program
        self.memory = program.memory
        self.call_preproc_ast = call_preproc_ast
        self.desc = desc

        self.user_defined_fn: dict[PreprocessingId, NormedUserDefinedFn] = {}

    def generate(self):
        for i in range(len(self.desc.preprocessing)):
            self._generate_preprocessing(i)

    def _generate_preprocessing(self, prepro_id: PreprocessingId):
        preprocessing = self.desc.preprocessing[prepro_id]
        genfn_name = f"preprocess_{prepro_id}"

        self.program.root.linebreak()
        prepro_fn = self.program.root.func(
            genfn_name,
            [
                Var.create(
                    self.memory,
                    "resource_data",
                    key=VarSpace.resource_data(preprocessing.value.resource_id),
                ),
            ],
        )

        if preprocessing.type == PreprocessingType.pmap:
            value = preprocessing.value
            assert isinstance(value, PMap)

            # generate the necessary function (user defined fn & our preprocessing fn)
            self._init_user_defined_fn(prepro_id, value.code)
            self._generate_preprocessing_pmap(prepro_id, prepro_fn, value)

            # call preprocessing fn in the main program
            self.call_preproc_ast.expr(
                expr.ExprFuncCall(
                    expr.ExprIdent(genfn_name),
                    [
                        expr.ExprVar(
                            Var.deref(
                                self.memory,
                                key=VarSpace.resource_data(
                                    preprocessing.value.resource_id
                                ),
                            )
                        ),
                    ],
                )
            )
            return None

        raise NotImplementedError(preprocessing.type)

    def _generate_preprocessing_pmap(self, prepro_id: int, prepro_fn: AST, value: PMap):
        if not value.change_structure and value.output is None:
            # if we don't change the structure and don't have output, we directly mutate the resource data
            # the idea is to loop through the path without the last index, get the value, apply the function, and set the value
            # of the last index to the new value.
            pseudo_attr = Attr(
                id=f"preproc_{prepro_id}_path",
                resource_id=value.resource_id,
                path=value.path,
                missing_values=[],
                unique=False,
                sorted=Sorted.Null,
                value_type=ValueType.UnspecifiedSingle,
            )
            ast = PathAccessor(self.program.import_manager).iterate_elements(
                mem=self.memory,
                ast=prepro_fn,
                attr=pseudo_attr,
            )

            # get item value & item context
            item_value = Var.deref(
                self.memory,
                key=VarSpace.attr_value_dim(
                    pseudo_attr.resource_id,
                    pseudo_attr.id,
                    len(pseudo_attr.path.steps) - 1,
                ),
            )
            if len(pseudo_attr.path.steps) > 1:
                parent_item_value = Var.deref(
                    self.memory,
                    key=VarSpace.attr_value_dim(
                        pseudo_attr.resource_id,
                        pseudo_attr.id,
                        len(pseudo_attr.path.steps) - 2,
                    ),
                )
            else:
                parent_item_value = Var.deref(
                    self.memory,
                    key=VarSpace.resource_data(pseudo_attr.resource_id),
                )

            if self.user_defined_fn[prepro_id].use_context:
                # TODO: implement this
                # item_context = expr.ExprFuncCall(
                #     expr.ExprIdent("ContextImpl"),
                #     [
                #         expr.ExprVar(
                #             Var.deref(
                #                 self.memory,
                #                 key=VarSpace.resource_data(pseudo_attr.resource_id),
                #             )
                #         ),
                #         expr.ExprVar(
                #             Var.deref(
                #                 self.memory,
                #                 key=VarSpace.attr_index_dim(
                #                     pseudo_attr.resource_id,
                #                     pseudo_attr.id,
                #                     len(pseudo_attr.path.steps) - 1,
                #                 ),
                #             )
                #         ),
                #     ],
                # )
                raise NotImplementedError()
            else:
                item_context = None

            # then we call the user defined fn to get the new item value
            new_item_value = self._call_user_defined_fn(
                prepro_id,
                ast,
                expr.ExprVar(item_value),
                item_context,
            )

            # then, we set the new item value to the parent item value
            ast.expr(
                DReprPredefinedFn.item_setter(
                    expr.ExprVar(parent_item_value),
                    expr.ExprVar(
                        Var.deref(
                            self.memory,
                            key=VarSpace.attr_index_dim(
                                pseudo_attr.resource_id,
                                pseudo_attr.id,
                                len(pseudo_attr.path.steps) - 1,
                            ),
                        )
                    ),
                    new_item_value,
                )
            )
        else:
            # we have to create a temporary variable to store preprocessed results
            raise NotImplementedError()

    def _init_user_defined_fn(self, prepro_id: PreprocessingId, code: str):
        """First, import statements are moved to the top of the file. The rest of the code can be either
        wrapped in a function (as expected in DRepr design), or directly embedded whenever it is used.

        The later option (embedding code) yields more performance, but it is harder because of potential variable name conflicts.
        To implement the embedding code, we need to parse the code to find all variables that are used in the code and
        ensure that they are not used or overwrite previous variables (potential renaming may require). Also, we need to rewrite
        the return statement.
        """
        # detect indentation & remove it
        parsed_udf = UDFParser(code).parse(["context"])

        # now create a function containing the user-defined function
        fnname = f"preproc_{prepro_id}_customfn"
        fnargs = [
            Var.create(
                self.memory,
                "value",
                key=VarSpace.preprocessing_udf_value(
                    self.desc.preprocessing[prepro_id].value.resource_id
                ),
            )
        ]
        use_context = "context" in parsed_udf.monitor_variables

        if use_context:
            fnargs.append(
                Var.create(
                    self.memory,
                    "context",
                    key=VarSpace.preprocessing_udf_context(
                        self.desc.preprocessing[prepro_id].value.resource_id
                    ),
                )
            )

        # create a function that will be used to create the user-defined function
        create_udf = self.program.root.func("get_" + fnname, [])
        for import_stmt in parsed_udf.imports:
            create_udf.python_stmt(import_stmt)

        inner_udf = create_udf.func(fnname, fnargs)

        def insert_source_tree(ast: AST, tree: SourceTree):
            assert tree.node != ""
            for child in tree.children:
                insert_source_tree(ast.python_stmt(child.node), child)

        assert parsed_udf.source_tree.node == ""
        insert_source_tree(inner_udf, parsed_udf.source_tree)

        inner_udf.return_(expr.ExprIdent(fnname))

        # now we create the user-defined function
        fnvar = Var.create(self.memory, fnname)
        self.program.root.assign(
            self.memory,
            fnvar,
            expr.ExprFuncCall(expr.ExprIdent("get_" + fnname), []),
        )

        self.user_defined_fn[prepro_id] = NormedUserDefinedFn(
            name=fnname, udf=parsed_udf, use_context=use_context, fnvar=fnvar
        )

    def _call_user_defined_fn(
        self,
        prepro_id: PreprocessingId,
        ast: AST,
        value: expr.Expr,
        context: Optional[expr.Expr],
    ) -> expr.Expr:
        """Call the user-defined function"""
        return expr.ExprFuncCall(
            expr.ExprVar(self.user_defined_fn[prepro_id].fnvar),
            [value, context] if context is not None else [value],
        )


class ContextImpl(Context):
    def __init__(self, resource_data, index: tuple):
        self.resource_data = resource_data
        self.index = index

    def get_index(self) -> tuple:
        return self.index

    def get_value(self, resource_data, index: tuple):
        ptr = self.resource_data
        for i in index:
            ptr = ptr[i]
        return ptr