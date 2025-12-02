from __future__ import annotations

import importlib
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field, replace
from functools import wraps
from inspect import Signature, signature
from typing import (
    Any,
    Generic,
    Literal,
    ParamSpec,
    TypeGuard,
    TypeVar,
    cast,
    overload,
)

from ordeq._fqn import FQN
from ordeq._io import (
    IO,
    AnyIO,
    Input,
    Output,
    ResourceType,
    _is_input,
    _is_output,
)
from ordeq.preview import preview

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
    if module:
        return f"{module}:{name}"
    return name


@dataclass(frozen=True, kw_only=True)
class Node(Generic[FuncParams, FuncReturns]):
    @property
    def __doc__(self) -> str | None:  # type: ignore[override]
        return self.func.__doc__

    func: Callable[FuncParams, FuncReturns]
    inputs: tuple[Input, ...]
    outputs: tuple[Output, ...]
    checks: tuple[AnyIO | ResourceType, ...] = ()
    attributes: dict[str, Any] = field(default_factory=dict, hash=False)
    views: tuple[View, ...] = ()

    # The node module and name is assigned:
    # 1. from the function if the node is created via the @node decorator
    # 2. otherwise, if possible, from the run/viz context
    module: str | None = None
    name: str | None = None

    def __post_init__(self):
        """Nodes always have to be hashable"""
        self.validate()

    def validate(self) -> None:
        """These checks are performed before the node is run."""
        _raise_if_not_hashable(self)
        _raise_for_invalid_inputs(self)
        _raise_for_invalid_outputs(self)

    def _patch_io(
        self, io: dict[AnyIO, AnyIO]
    ) -> Node[FuncParams, FuncReturns]:
        """Patches the inputs and outputs of the node with the provided IO
        mapping.

        Args:
            io: mapping of Input/Output objects to their replacements

        Returns:
            the node with patched inputs and outputs
        """

        return replace(
            self,
            inputs=tuple(io.get(ip, ip) for ip in self.inputs),  # type: ignore[misc,arg-type]
            outputs=tuple(io.get(op, op) for op in self.outputs),  # type: ignore[misc,arg-type]
        )

    @property
    def is_fq(self) -> bool:
        return self.name is not None and self.module is not None

    @property
    def func_name(self) -> str:
        return infer_node_name_from_func(self.func)

    @property
    def ref(self) -> str:
        if self.is_fq:
            return format(self.fqn, "ref")
        return f"{self.__class__.__name__}(func={self.func_name}, ...)"

    @property
    def fqn(self) -> FQN | None:
        if self.is_fq:
            return FQN(module=self.module, name=self.name)  # type: ignore[arg-type]
        return None

    @property
    def type_name(self) -> Literal["Node", "View"]:
        return type(self).__name__  # type: ignore[return-value]

    def __call__(self, *args, **kwargs) -> FuncReturns:
        return self.func(*args, **kwargs)  # type: ignore[invalid-return-type]

    def __repr__(self) -> str:
        if self.is_fq:
            attributes = {"module": self.module, "name": self.name}
        else:
            attributes = {"func": self.func_name}

        inputs = getattr(self, "inputs", None)
        if inputs:
            input_str = ", ".join(repr(i) for i in inputs)
            attributes["inputs"] = f"[{input_str}]"

        outputs = getattr(self, "outputs", None)
        if outputs:
            output_str = ", ".join(repr(o) for o in outputs)
            attributes["outputs"] = f"[{output_str}]"

        if self.attributes:
            attributes["attributes"] = repr(self.attributes)

        attributes_str = ", ".join(f"{k}={v}" for k, v in attributes.items())
        return f"{self.type_name}({attributes_str})"

    def __str__(self) -> str:
        if self.is_fq:
            return f"{self.type_name.lower()} {self.fqn:desc}"
        return f"{self.type_name}(func={self.func_name}, ...)"


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
            f"Inputs invalid for function arguments of {n}"
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

    are_outputs = [_is_output(o) for o in n.outputs]
    if not all(are_outputs):
        not_an_output = n.outputs[are_outputs.index(False)]
        raise ValueError(
            f"Outputs of {n} must be of type Output, "
            f"got {type(not_an_output).__name__} "
        )

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
            f"Outputs invalid for return annotation: {n}. "
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
        raise ValueError(f"{n} is not hashable") from e


def _sequence_to_tuple(obj: Sequence[T] | T | None) -> tuple[T, ...]:
    if obj is None:
        return ()
    if isinstance(obj, Sequence):
        return tuple(obj)  # ty: ignore[invalid-return-type]
    return (obj,)  # ty: ignore[invalid-return-type]


@dataclass(frozen=True, kw_only=True)
class View(Node[FuncParams, FuncReturns]):
    outputs: tuple[IO, ...] = ()

    def __post_init__(self):
        self.validate()

    def _patch_io(
        self, io: dict[AnyIO, AnyIO]
    ) -> View[FuncParams, FuncReturns]:
        """Patches the inputs  of the view with the provided IO mapping.

        Args:
            io: mapping of Input/Output objects to their replacements

        Returns:
            the node with patched inputs
        """

        return replace(
            self,
            inputs=tuple(io.get(ip, ip) for ip in self.inputs),  # type: ignore[misc]
        )

    def __repr__(self) -> str:
        if self.name and self.module:
            attributes = {"module": self.module, "name": self.name}
        else:
            attributes = {"func": infer_node_name_from_func(self.func)}

        inputs = getattr(self, "inputs", None)
        if inputs:
            input_str = ", ".join(repr(i) for i in inputs)
            attributes["inputs"] = f"[{input_str}]"

        if self.attributes:
            attributes["attributes"] = repr(self.attributes)

        attributes_str = ", ".join(f"{k}={v}" for k, v in attributes.items())

        return f"View({attributes_str})"


def _is_node(obj: object) -> TypeGuard[Node]:
    return isinstance(obj, Node)


def _is_view(obj: object) -> TypeGuard[View]:
    return isinstance(obj, View)


@overload
def create_node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: Sequence[Output] | Output,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    attributes: dict[str, Any] | None = None,
    module: str | None = None,
    name: str | None = None,
) -> Node[FuncParams, FuncReturns]: ...


@overload
def create_node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: None = None,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    attributes: dict[str, Any] | None = None,
    module: str | None = None,
    name: str | None = None,
) -> View[FuncParams, FuncReturns]: ...


def create_node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: Sequence[Output] | Output | None = None,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    attributes: dict[str, Any] | None = None,
    module: str | None = None,
    name: str | None = None,
) -> Node[FuncParams, FuncReturns] | View[FuncParams, FuncReturns]:
    """Creates a Node instance.

    Args:
        func: The function to be executed by the node.
        inputs: The inputs to the node.
        outputs: The outputs from the node.
        checks: The checks for the node.
        attributes: Optional attributes for the node.
        module: Module name for the node.
        name: Name for the node.

    Returns:
        A Node instance.

    Raises:
        ValueError: if any of the inputs is a callable that is not a view
    """

    func_name = infer_node_name_from_func(func)
    inputs_: list[Input] = []
    views: list[View] = []
    cls = "View" if not outputs else "Node"
    for obj in _sequence_to_tuple(inputs):
        if _is_view(obj):
            views.append(obj)
            inputs_.append(obj.outputs[0])
        elif _is_input(obj):
            inputs_.append(obj)
        else:
            raise ValueError(
                f"Inputs to {cls}(func={func_name}, ...) must be an "
                f"Input or View, got {type(obj).__name__}"
            )

    checks_: list[Input] = []
    if checks:
        preview(
            "Checks are in preview mode and may change "
            "without notice in future releases."
        )

        for check in _sequence_to_tuple(checks):
            if callable(check):
                if not _is_node(check):
                    raise ValueError(
                        f"Check {check} to node {cls}(func={func_name}, ...) "
                        f"is not a node"
                    )
                view = check
                if not isinstance(view, View):
                    raise ValueError(
                        f"Check {check} to node {cls}(func={func_name}, ...) "
                        f"is not a view"
                    )
                checks_.append(view.outputs[0])
            else:
                checks_.append(cast("Input", check))

    if not outputs:
        return View(
            func=func,  # type: ignore[arg-type]
            inputs=tuple(inputs_),  # type: ignore[arg-type]
            outputs=(IO(),),  # type: ignore[arg-type]
            checks=tuple(checks_),  # type: ignore[arg-type]
            attributes={} if attributes is None else attributes,  # type: ignore[arg-type]
            views=tuple(views),  # type: ignore[arg-type]
            module=module,  # type: ignore[arg-type]
            name=name,  # type: ignore[arg-type]
        )
    return Node(
        func=func,
        inputs=tuple(inputs_),
        outputs=_sequence_to_tuple(outputs),
        checks=tuple(checks_),  # type: ignore[arg-type]
        attributes={} if attributes is None else attributes,
        views=tuple(views),
        module=module,
        name=name,
    )


# Default value for 'func' in case it is not passed.
# Used to distinguish between 'func=None' and func missing as positional arg.
def _not_passed(*args, **kwargs): ...


not_passed = cast("View", _not_passed)


@overload
def node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: Sequence[Output] | Output,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    **attributes: Any,
) -> Node[FuncParams, FuncReturns]: ...


@overload
def node(
    func: Callable[FuncParams, FuncReturns],
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: None = None,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    **attributes: Any,
) -> View[FuncParams, FuncReturns]: ...


@overload
def node(
    *,
    inputs: Sequence[Input | View] | Input | View = not_passed,
    outputs: Sequence[Output] | Output,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    **attributes: Any,
) -> Callable[
    [Callable[FuncParams, FuncReturns]], Node[FuncParams, FuncReturns]
]: ...


@overload
def node(
    *,
    inputs: Sequence[Input | View] | Input | View = not_passed,
    outputs: None = None,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    **attributes: Any,
) -> Callable[
    [Callable[FuncParams, FuncReturns]], View[FuncParams, FuncReturns]
]: ...


def node(
    func: Callable[FuncParams, FuncReturns] = _not_passed,
    *,
    inputs: Sequence[Input | View] | Input | View | None = None,
    outputs: Sequence[Output] | Output | None = None,
    checks: Sequence[Input | Output | Node]
    | Input
    | Output
    | Node
    | ResourceType
    | None = None,
    **attributes: Any,
) -> (
    Callable[
        [Callable[FuncParams, FuncReturns]],
        Node[FuncParams, FuncReturns] | View[FuncParams, FuncReturns],
    ]
    | Node[FuncParams, FuncReturns]
    | View[FuncParams, FuncReturns]
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

    You can assign attributes to a node, which can be used for filtering or
    grouping nodes later:

    ```python
    >>> @node(inputs=..., outputs=..., group="group1", retries=3)
    ... def func(...): -> ...

    ```

    Args:
        func: function of the node
        inputs: sequence of inputs
        outputs: sequence of outputs
        checks: sequence of checks
        attributes: additional attributes to assign to the node

    Returns:
        a node

    Raises:
        ValueError: if 'input' or 'output' is provided as keyword argument

    """

    if "input" in attributes:
        raise ValueError(
            "The 'input' keyword argument is not supported. "
            "Did you mean 'inputs'?"
        )
    if "output" in attributes:
        raise ValueError(
            "The 'output' keyword argument is not supported. "
            "Did you mean 'outputs'?"
        )

    if func is None or not callable(func):
        raise ValueError(
            f"The first argument to node must be a function, "
            f"got {type(func).__name__}"
        )

    if func is not_passed:
        # we are called as @node(inputs=...

        def wrapped(
            f: Callable[FuncParams, FuncReturns],
        ) -> Node[FuncParams, FuncReturns]:
            @wraps(f)
            def inner(*args: FuncParams.args, **kwargs: FuncParams.kwargs):
                # Purpose of this inner is to create a new function from `f`
                return f(*args, **kwargs)

            node_ = create_node(
                inner,
                inputs=inputs,
                outputs=outputs,
                checks=checks,
                attributes=attributes,
                module=f.__module__,
                name=f.__name__,
            )
            node_.__dict__["__annotations__"] = f.__annotations__  # noqa: RUF063
            return node_

        return wrapped

    # else: we are called as node(func, inputs=...) or @node (without kwargs)

    @wraps(func)
    def wrapper(
        *args: FuncParams.args, **kwargs: FuncParams.kwargs
    ) -> FuncReturns:
        # The purpose of this wrapper is to create a new function from `func`
        return func(*args, **kwargs)

    node_ = create_node(
        wrapper,
        inputs=inputs,
        outputs=outputs,
        checks=checks,
        attributes=attributes,
    )

    node_.__dict__["__annotations__"] = func.__annotations__  # noqa: RUF063

    return node_
