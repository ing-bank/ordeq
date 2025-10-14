from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from functools import wraps
from logging import getLogger
from typing import Any, Generic, ParamSpec, TypeVar, overload

from ordeq._io import IO, Input

logger = getLogger("ordeq.nodes")

FuncParams = ParamSpec("FuncParams")
FuncReturns = TypeVar("FuncReturns")


class Sentinel(IO):
    def load(self) -> None:
        return None

    def save(self, data: None) -> None:
        pass

    def __repr__(self) -> str:
        return "Sentinel()"


@dataclass(frozen=True, kw_only=True)
class View(Generic[FuncParams, FuncReturns]):
    func: Callable[FuncParams, FuncReturns]
    inputs: tuple[Input | View, ...]
    tags: list[str] | dict[str, Any] = field(default_factory=list, hash=False)
    sentinel: IO = field(default_factory=Sentinel, repr=False)

    def __repr__(self):
        return f"View(func={self.func.__name__}, inputs={self.inputs})"

    @classmethod
    def create(
        cls,
        func: Callable[FuncParams, FuncReturns],
        inputs: Sequence[Input | View],
        tags: list[str] | dict[str, Any] | None = None,
    ) -> View:
        """Factory method to create a View instance.

        Args:
            func: The function to be wrapped in the view.
            inputs: Input or View instances serving as inputs to the view.
            tags: Optional tags to assign to the view.

        Return:
            A View instance.

        """

        return cls(
            func=func, inputs=tuple(inputs) if inputs else tuple(), tags=tags
        )

    def replace(
        self,
        *,
        func: Callable[FuncParams, FuncReturns] | None = None,
        inputs: Sequence[Input | View] | None = None,
    ) -> View[FuncParams, FuncReturns]:
        return View(func=func or self.func, inputs=inputs or self.inputs)


@overload
def view(
    func: Callable[FuncParams, FuncReturns],
    *inputs: Input | Callable,
    tags: list[str] | dict[str, Any] | None = None,
) -> Callable[FuncParams, FuncReturns]: ...


@overload
def view(
    *inputs: Input | Callable, tags: list[str] | dict[str, Any] | None = None
) -> Callable[
    [Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]
]: ...


def view(
    func: Callable[FuncParams, FuncReturns] | None = None,
    *inputs: Input | Callable,
    tags: list[str] | dict[str, Any] | None = None,
) -> (
    Callable[
        [Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]
    ]
    | Callable[FuncParams, FuncReturns]
):
    """Decorator that creates a view from a function.

    Args:
        func: function of the node
        inputs: sequence of inputs
        tags: tags to assign to the node

    Returns:
        a view
    """

    if func is None:
        # we are called as @view(inputs=...
        def wrapped(
            f: Callable[FuncParams, FuncReturns],
        ) -> Callable[FuncParams, FuncReturns]:
            @wraps(f)
            def inner(*args, **kwargs):
                # Purpose of this inner is to create a new function from `f`
                return f(*args, **kwargs)

            inner.__ordeq_view__ = View.create(  # type: ignore[attr-defined]
                inner, inputs=inputs, tags=tags
            )
            return inner

        return wrapped

    # else: we are called as view(func, inputs=...)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # The purpose of this wrapper is to create a new function from `func`
        return func(*args, **kwargs)

    wrapper.__ordeq_view__ = View.create(  # type: ignore[attr-defined]
        wrapper, inputs=inputs, tags=tags
    )
    return wrapper
