from __future__ import annotations

from typing import Optional, TypeVar

V = TypeVar("V")


def assert_not_null(x: Optional[V]) -> V:
    assert x is not None
    return x


def assert_true(x: bool, msg: str) -> bool:
    assert x, msg
    return True
