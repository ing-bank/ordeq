import importlib
import logging
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from functools import wraps
from inspect import Signature, signature
from typing import Any, Generic, ParamSpec, TypeVar, overload

from ordeq._io import Input, Output

logger = logging.getLogger("ordeq.nodes")

T = TypeVar("T")
FuncParams = ParamSpec("FuncParams")
FuncReturns = TypeVar("FuncReturns")


def infer_node_name_from_func(func: Callable[..., Any]) -> str:
    """Infers a node name from a function, including its module.

    Args:
        func: The function to infer the name from.

    Returns:
        The inferred name.
    """

    name = func.__name__
    module = getattr(func, "__module__", None)
    if module and module != "__main__":
        return f"{module}:{name}"
    return name


@dataclass(frozen=True, kw_only=True)
class Node(Generic[FuncParams, FuncReturns]):
    func: Callable[FuncParams, FuncReturns]
    name: str
    inputs: tuple[Input, ...]
    outputs: tuple[Output, ...]
    tags: list[str] | dict[str, Any] = field(default_factory=list, hash=False)

    def __post_init__(self):
        """Nodes always have to be hashable"""
        _raise_if_not_hashable(self)
        if self.inputs:
            _raise_for_invalid_inputs(self)
        if self.outputs:
            _raise_for_invalid_outputs(self)

    def validate(self) -> None:
        """These checks are performed before the node is run."""
        _raise_for_invalid_inputs(self)
        _raise_for_invalid_outputs(self)

    def __repr__(self) -> str:
        attributes = {"name": self.name}

        inputs = getattr(self, "inputs", None)
        if inputs:
            input_str = ", ".join(repr(i) for i in inputs)
            attributes["inputs"] = f"[{input_str}]"

        outputs = getattr(self, "outputs", None)
        if outputs:
            output_str = ", ".join(repr(o) for o in outputs)
            attributes["outputs"] = f"[{output_str}]"

        if self.tags:
            attributes["tags"] = repr(self.tags)

        attributes_str = ", ".join(f"{k}={v}" for k, v in attributes.items())
        return f"Node({attributes_str})"

    def _replace(
        self,
        *,
        name: str | None = None,
        inputs: Sequence[Input] | Input | None = None,
        outputs: Sequence[Output] | Output | None = None,
    ) -> "Node[FuncParams, FuncReturns]":
        return Node(
            func=self.func,
            name=name or self.name,
            inputs=_sequence_to_tuple(inputs or self.inputs),
            outputs=_sequence_to_tuple(outputs or self.outputs),
            tags=self.tags,
        )


def _raise_for_invalid_inputs(n: Node) -> None:
    """Raises a ValueError if the number of inputs is incompatible with
    node arguments.

    Args:
        n: a Node

    Raises:
        ValueError: if the number of inputs is incompatible with the number of
            node arguments.
    """

    func = n.func
    sign = signature(func)
    try:
        sign.bind(*n.inputs)
    except TypeError as e:
        raise ValueError(
            f"Node inputs invalid for function arguments: "
            f"Node(name={n.name},...)"
        ) from e


def _raise_for_invalid_outputs(n: Node) -> None:
    """Raises a ValueError if the number of outputs is incompatible with
    node arguments.

    Args:
        n: a Node

    Raises:
        ValueError: if the number of outputs is incompatible with the number of
            node arguments.
    """
    func = n.func
    sign = signature(func)
    returns = sign.return_annotation
    if returns == Signature.empty:
        return

    # deal with `from __future__ import annotations`
    if isinstance(returns, str):
        try:
            mod = importlib.import_module(func.__module__)
            returns = eval(returns, mod.__dict__)  # noqa: S307
        except (NameError, ImportError):
            return

    # any return type is valid for a single output
    if len(n.outputs) == 1:
        return

    # A type annotation was provided
    if returns is None:
        return_types = []
    elif hasattr(returns, "__origin__") and returns.__origin__ is tuple:
        # tuple[pd.DataFrame, list[str]] => 2
        return_types = returns.__args__
    else:
        return_types = [returns]

    if len(return_types) != len(n.outputs):
        raise ValueError(
            "Node outputs invalid for return annotation: "
            f"Node(name={n.name},...). "
            f"Node has {len(n.outputs)} output(s), but the return type "
            f"annotation expects {len(return_types)} value(s)."
        )


def _raise_if_not_hashable(n: Node) -> None:
    """Raises a ValueError if a node is not hashable.

    Args:
        n: a Node

    Raises:
        ValueError: if the node is not hashable
    """

    try:
        hash(n)
    except TypeError as e:
        raise ValueError(
            f"Node is not hashable: Node(name={n.name}, ...)"
        ) from e


def _sequence_to_tuple(obj: Sequence[T] | T | None) -> tuple[T, ...]:
    if obj is None:
        return ()
    if isinstance(obj, Sequence):
        return tuple(obj)
    return (obj,)  # ty: ignore[invalid-return-type]


def _create_node(
    func: Callable[FuncParams, FuncReturns],
    *,
    name: str | None = None,
    inputs: Sequence[Input] | Input | None = None,
    outputs: Sequence[Output] | Output | None = None,
    tags: list[str] | dict[str, Any] | None = None,
) -> Node[FuncParams, FuncReturns]:
    """Creates a Node instance.

    Args:
        func: The function to be executed by the node.
        name: Optional name for the node. If not provided, inferred from func.
        inputs: The inputs to the node.
        outputs: The outputs from the node.
        tags: Optional tags for the node.

    Returns:
        A Node instance.
    """

    resolved_name = (
        name if name is not None else infer_node_name_from_func(func)
    )
    return Node(
        func=func,
        name=resolved_name,
        inputs=_sequence_to_tuple(inputs),
        outputs=_sequence_to_tuple(outputs),
        tags=[] if tags is None else tags,
    )


@overload
def node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input] | Input | None = None,
    outputs: Sequence[Output] | Output | None = None,
    tags: list[str] | dict[str, Any] | None = None,
) -> Callable[FuncParams, FuncReturns]: ...


@overload
def node(
    *,
    inputs: Sequence[Input] | Input | None = None,
    outputs: Sequence[Output] | Output | None = None,
    tags: list[str] | dict[str, Any] | None = None,
) -> Callable[
    [Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]
]: ...


def node(
    func: Callable[FuncParams, FuncReturns] | None = None,
    *,
    inputs: Sequence[Input] | Input | None = None,
    outputs: Sequence[Output] | Output | None = None,
    tags: list[str] | dict[str, Any] | None = None,
) -> (
    Callable[
        [Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]
    ]
    | Callable[FuncParams, FuncReturns]
):
    """Decorator that creates a node from a function. When a node is run,
    the inputs are loaded and passed to the function. The returned values
    are saved to the outputs.

    Example:

    ```python
    >>> from pyspark.sql import DataFrame
    >>> @node(
    ...     inputs=CSV(path="path/to.csv"),
    ...     outputs=Table(table="db.table")
    ... )
    ... def transformation(csv: DataFrame) -> DataFrame:
    ...     return csv.select("someColumn")

    ```

    Nodes can also take a variable number of inputs:

    ```python
    >>> @node(
    ...     inputs=[
    ...         CSV(path="path/to/fst.csv"),
    ...         # ...
    ...         CSV(path="path/to/nth.csv")
    ...     ],
    ...     outputs=Table(table="db.all_appended")
    ... )
    ... def append_dfs(*args: DataFrame) -> DataFrame:
    ...     df = args[0]
    ...     for arg in args[1:]:
    ...         df = df.unionByName(arg)
    ...     return df

    ```

    Node can also be created from existing functions:

    ```python
    >>> def remove_header(data: list[str]) -> list[str]:
    ...     return data[1:]
    >>> fst = node(remove_header, inputs=CSV(path="path/to/fst.csv"), ...)
    >>> snd = node(remove_header, inputs=CSV(path="path/to/snd.csv"), ...)
    >>> ...

    ```

    You can assign tags to a node, which can be used for filtering or grouping
    nodes later:

    ```python
    >>> @node(inputs=..., outputs=..., tags=["tag1", "tag2"])
    ... def func(...): -> ...

    ```

    Args:
        func: function of the node
        inputs: sequence of inputs
        outputs: sequence of outputs
        tags: tags to assign to the node

    Returns:
        a node

    """

    if func is None:
        # we are called as @node(inputs=...
        def wrapped(
            f: Callable[FuncParams, FuncReturns],
        ) -> Callable[FuncParams, FuncReturns]:
            @wraps(f)
            def inner(*args, **kwargs):
                # Purpose of this inner is to create a new function from `f`
                return f(*args, **kwargs)

            inner.__ordeq_node__ = _create_node(  # type: ignore[attr-defined]
                inner, inputs=inputs, outputs=outputs, tags=tags
            )
            return inner

        return wrapped

    # else: we are called as node(func, inputs=...)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # The purpose of this wrapper is to create a new function from `func`
        return func(*args, **kwargs)

    wrapper.__ordeq_node__ = _create_node(  # type: ignore[attr-defined]
        wrapper, inputs=inputs, outputs=outputs, tags=tags
    )
    return wrapper


def get_node(func: Callable) -> Node:
    """Gets the node from a callable created with the `@node` decorator.

    Args:
        func: a callable created with the `@node` decorator

    Returns:
        the node associated with the callable

    Raises:
        ValueError: if the callable was not created with the `@node` decorator
    """

    try:
        return func.__ordeq_node__  # type: ignore[attr-defined]
    except AttributeError as e:
        raise ValueError(f"'{func.__name__}' is not a node") from e
