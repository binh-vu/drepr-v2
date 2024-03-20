from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from codegen.models import PredefinedFn
from codegen.models.expr import Expr, ExprFuncCall, ExprIdent, ExprVar
from codegen.models.memory import Var
from codegen.models.program import ImportManager

from drepr.models.resource import ResourceType


class DReprPredefinedFn(PredefinedFn):

    @dataclass
    class _safe_item_getter(Expr):
        collection: Expr
        item: Expr
        msg: Expr

        def to_python(self):
            return f"safe_item_getter({self.collection.to_python()}, {self.item.to_python()}, {self.msg.to_python()})"

    @dataclass
    class _safe_len(Expr):
        collection: Expr
        msg: Expr

        def to_python(self):
            return f"safe_len({self.collection.to_python()}, {self.msg.to_python()})"

    @staticmethod
    def safe_item_getter(
        import_manager: ImportManager, collection: Expr, item: Expr, msg: Expr
    ):
        import_manager.import_("drepr.utils.safe.safe_item_getter", True)
        return DReprPredefinedFn._safe_item_getter(collection, item, msg)

    @staticmethod
    def safe_len(import_manager: ImportManager, collection: Expr, msg: Expr):
        import_manager.import_("drepr.utils.safe.safe_len", True)
        return DReprPredefinedFn._safe_len(collection, msg)

    @staticmethod
    def read_source(
        import_manager: ImportManager, source_type: ResourceType, input_file: Var
    ):
        import_manager.import_(
            f"drepr.readers.prelude.read_source_{source_type.value}", True
        )
        return ExprFuncCall(
            ExprIdent(f"read_source_{source_type.value}"), [ExprVar(input_file)]
        )
