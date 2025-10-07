from __future__ import annotations

import copy
import inspect
import logging
from collections.abc import Callable, Sequence
from functools import cached_property, reduce, wraps
from typing import Any, Generic, TypeVar
from uuid import uuid4

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

from ordeq.framework.hook import InputHook, OutputHook

logger = logging.getLogger(__name__)


class IOException(Exception):
    """Exception raised by IO implementations in case of load/save failure.
    IO implementations should provide instructive information.
    """


T = TypeVar("T")
Tin = TypeVar("Tin")
Tout = TypeVar("Tout")


def _find_references(attributes) -> dict[str, list[Input | Output | IO]]:
    """Find all attributes of type Input, Output, or IO.

    Args:
        attributes: a dictionary of attributes to inspect

    Returns:
        a dictionary mapping attribute names to lists of Input, Output, or IO
    """

    def get_io_instance(value: Any) -> list[Input | Output | IO]:
        if isinstance(value, (Input, Output, IO)):
            return [value]
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            return [io for v in value for io in get_io_instance(v)]
        if isinstance(value, dict):
            return [io for v in value.values() for io in get_io_instance(v)]
        return []

    wrapped = {}
    for attribute, value in attributes.items():
        ios = get_io_instance(value)
        if ios:
            wrapped[attribute] = ios
    return wrapped


def _raise_not_implemented(*args, **kwargs):
    raise NotImplementedError()


def _load_decorator(load_func):
    @wraps(load_func)
    def wrapper(self, *args, **kwargs):
        # wrappers defined in the base classes
        # similar to super().load_wrapper() calls, without requiring
        # the `load_wrappers` to call each super.
        wrappers = [
            base.load_wrapper
            for base in reversed(type(self).__mro__)
            if hasattr(base, "load_wrapper")
        ]

        def base_func(*a, **k):
            logger.info("Loading %s", self)

            return load_func(self, *a, **k)

        composed = reduce(
            lambda prev_func, wrap: lambda *a, **k: wrap(
                self, prev_func, *a, **k
            ),
            wrappers,
            base_func,
        )
        return composed(*args, **kwargs)

    return wrapper


class _InputMeta(type):
    def __new__(cls, name, bases, class_dict):
        # Retrieve the closest load method
        load_method = _raise_not_implemented
        for base in bases:
            l_method = getattr(base, "load", None)
            if (
                l_method is not None
                and l_method.__qualname__ != "_raise_not_implemented"
            ):
                load_method = l_method

        l_method = class_dict.get("load", None)
        if (
            l_method is not None
            and l_method.__qualname__ != "_raise_not_implemented"
        ):
            load_method = l_method

        if name not in {"Input", "IO"}:
            # Ensure load method is implemented
            if (
                not callable(load_method)
                or load_method.__qualname__ == "_raise_not_implemented"
            ):
                msg = (
                    f"Can't instantiate abstract class {name} "
                    "with abstract method load"
                )
                raise TypeError(msg)

            # Ensure all arguments (except self/cls) have default values
            sig = inspect.signature(load_method)
            for argument, param in sig.parameters.items():
                if argument in {"self", "cls"}:
                    continue
                if (
                    param.default is inspect.Parameter.empty
                    and param.kind != inspect._ParameterKind.VAR_KEYWORD  # noqa: SLF001
                ):
                    raise TypeError(
                        f"Argument '{argument}' of function "
                        f"'{load_method.__name__}' has no default value."
                    )

        if not hasattr(load_method, "__wrapped__"):
            class_dict["load"] = _load_decorator(load_method)
        return super().__new__(cls, name, bases, class_dict)


class _BaseInput(Generic[Tin]):
    load: Callable = _raise_not_implemented


class _InputOptions(_BaseInput[Tin]):
    """Class that adds load options to an Input.
    Used for compartmentalizing load options, no reuse."""

    _load_options: dict[str, Any] | None = None

    def with_load_options(self, **load_options) -> Self:
        """Creates a new instance of self with load options set to kwargs.

        Note:
            the instance is shallow-copied. The new instance still references
            the attributes of the original instance.

        Returns:
            a new instance, with load options set to kwargs
        """

        new_instance = copy.copy(self)

        # ensure the `load_options` are valid for the `load` method
        inspect.signature(new_instance.load).bind_partial(**load_options)

        # Set the dict directly to support IO that are frozen dataclasses:
        new_instance.__dict__["_load_options"] = load_options
        return new_instance

    def load_wrapper(self, load_func, *args, **kwargs) -> Tin:
        # Compose load options and pass to the load_func
        load_options = self._load_options or {}

        # Kwargs take priority of load_options
        load_options.update(kwargs)
        return load_func(*args, **load_options)


class _InputHooks(_BaseInput[Tin]):
    """Class that adds input hooks to an Input.
    Used for compartmentalizing load options, no reuse."""

    input_hooks: tuple[InputHook, ...] = ()

    def with_input_hooks(self, *hooks: InputHook) -> Self:
        for hook in hooks:
            if not (
                isinstance(hook, InputHook) and not isinstance(hook, type)
            ):
                raise TypeError(f"Expected InputHook instance, got {hook}.")

        new_instance = copy.copy(self)
        new_instance.__dict__["input_hooks"] = hooks
        return new_instance

    def load_wrapper(self, load_func, *args, **kwargs) -> Tin:
        for hook in self.input_hooks:
            hook.before_input_load(self)  # type: ignore[arg-type]

        result = load_func(*args, **kwargs)

        for hook in self.input_hooks:
            hook.after_input_load(self, result)  # type: ignore[arg-type]

        return result


class _InputReferences(_BaseInput[Tin]):
    """Class that adds reference tracking to an Input.
    Used for compartmentalizing reference tracking, no reuse."""

    @cached_property
    def references(self) -> dict[str, list[Input | Output | IO]]:
        """Find all attributes of type Input, Output, or IO on the object.

        Returns:
            a dictionary mapping attribute names to lists of Input, Output,
            or IO
        """
        return _find_references(self.__dict__)


class _InputCache(_BaseInput[Tin]):
    """Class that adds caching to an Input."""

    _data: Tin

    def load_wrapper(self, load_func, *args, **kwargs) -> Tin:
        if not hasattr(self, "_data"):
            return load_func(*args, **kwargs)
        return self._data

    def persist(self, data: Tin) -> None:
        self.__dict__["_data"] = data

    def unpersist(self) -> None:
        if "_data" in self.__dict__:
            del self.__dict__["_data"]


class _InputException(_BaseInput[Tin]):
    def load_wrapper(self, load_func, *args, **kwargs) -> Tin:
        try:
            return load_func(*args, **kwargs)
        except Exception as exc:
            msg = f"Failed to load {self!s}.\n{exc!s}"
            raise IOException(msg) from exc


class Input(
    _InputOptions[Tin],
    _InputHooks[Tin],
    _InputReferences[Tin],
    _InputCache[Tin],
    _InputException[Tin],
    Generic[Tin],
    metaclass=_InputMeta,
):
    """Base class for all inputs in Ordeq. An `Input` is a class that loads
    data. All `Input` classes should implement a load method. By default,
    loading an input raises a `NotImplementedError`. See the Ordeq IO packages
    for some out-of-the-box implementations (e.g., `Literal`, `StringBuffer`,
    etc.).

    `Input` can also be used directly as placeholder. This can be useful when
    you are defining a node, but you do not want to provide an actual input
    yet. In this case, you can:

    ```python
    >>> from ordeq.framework import Input, node
    >>> from ordeq_common import StringBuffer

    >>> name = Input[str]()
    >>> greeting = StringBuffer()

    >>> @node(
    ...     inputs=name,
    ...     outputs=greeting
    ... )
    ... def greet(name: str) -> str:
    ...     return f"Hello, {name}!"

    ```

    In the example above, `name` represents the placeholder input to the node
    `greet`. Running the node greet as-is will raise a `NotImplementedError`:

    ```python
    >>> from ordeq import run
    >>> run(greet) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    NotImplementedError:

    ```

    To use the `greet` node, we need to provide an actual input. For instance:

    ```python
    >>> from ordeq_common import Literal
    >>> result = run(greet, io={name: Literal("Alice")})
    >>> result[greeting]
    'Hello, Alice!'
    ```
    """

    def __init__(self):
        self._idx = str(uuid4())

    def __repr__(self):
        return f"Input(idx={self._idx})"


def _save_decorator(save_func):
    @wraps(save_func)
    def wrapper(self, data, /, *args, **kwargs):
        # wrappers defined in the base classes
        # similar to super().save_wrapper() calls, without requiring
        # the `save_wrapper` to call each super.
        wrappers = [
            base.save_wrapper
            for base in reversed(type(self).__mro__)
            if hasattr(base, "save_wrapper")
        ]

        def base_func(d, *a, **k):
            logger.info("Saving %s", self)

            save_func(self, d, *a, **k)

        composed = reduce(
            lambda prev_func, wrap: lambda d, *a, **k: wrap(
                self, prev_func, d, *a, **k
            ),
            wrappers,
            base_func,
        )
        composed(data, *args, **kwargs)

    return wrapper


class _OutputMeta(type):
    def __new__(cls, name, bases, class_dict):
        # Retrieve the closest save method
        save_method = _raise_not_implemented
        for base in bases:
            s_method = getattr(base, "save", None)
            if s_method is not None and s_method.__qualname__ != "_pass":
                save_method = s_method

        s_method = class_dict.get("save", None)
        if s_method is not None and s_method.__qualname__ != "_pass":
            save_method = s_method

        if name not in {"Output", "IO"}:
            if not callable(save_method) or save_method == _pass:
                msg = (
                    f"Can't instantiate abstract class {name} "
                    "with abstract method save"
                )
                raise TypeError(msg)

            sig = inspect.signature(save_method)
            if len(sig.parameters) < 2:
                raise TypeError("Save method requires a data parameter.")

            # Ensure all arguments (except the first two, self/cls and data)
            # have default values
            for i, (argument, param) in enumerate(sig.parameters.items()):
                # Skip self/cls and data
                if i < 2:
                    continue
                if (
                    param.default is inspect.Parameter.empty
                    and param.kind != inspect._ParameterKind.VAR_KEYWORD  # noqa: SLF001
                ):
                    raise TypeError(
                        f"Argument '{argument}' of function "
                        f"'{save_method.__name__}' has no default value."
                    )

            if (
                sig.return_annotation != inspect.Signature.empty
                and sig.return_annotation is not None
            ):
                raise TypeError("Save method must have return type None.")

            if not hasattr(save_method, "__wrapped__"):
                class_dict["save"] = _save_decorator(save_method)
        return super().__new__(cls, name, bases, class_dict)


def _pass(*args, **kwargs):
    return


class _BaseOutput(Generic[Tout]):
    save: Callable = _pass


class _OutputOptions(_BaseOutput[Tout], Generic[Tout]):
    """Class that adds save options to an Output.
    Used for compartmentalizing save options, no reuse."""

    _save_options: dict[str, Any] | None = None

    def with_save_options(self, **save_options) -> Self:
        """Creates a new instance of self with save options set to kwargs.

        Note:
            the instance is shallow-copied. The new instance still references
            the attributes of the original instance.

        Returns:
            a new instance, with save options set to kwargs
        """

        new_instance = copy.copy(self)

        # ensure the `save_options` are valid for the `save` method
        inspect.signature(new_instance.save).bind_partial(**save_options)

        # Set the dict directly to support IO that are frozen dataclasses
        new_instance.__dict__["_save_options"] = save_options
        return new_instance

    def save_wrapper(self, save_func, data: Tout, *args, **kwargs) -> None:
        save_options = self._save_options or {}

        # Kwargs take priority of save_options
        save_options.update(kwargs)
        save_func(data, *args, **save_options)


class _OutputHooks(_BaseOutput[Tout], Generic[Tout]):
    """Class that adds output hooks to an Output.
    Used for compartmentalizing load options, no reuse."""

    output_hooks: tuple[OutputHook, ...] = ()

    def with_output_hooks(self, *hooks: OutputHook) -> Self:
        for hook in hooks:
            if not (
                isinstance(hook, OutputHook) and not isinstance(hook, type)
            ):
                raise TypeError(f"Expected OutputHook instance, got {hook}.")

        new_instance = copy.copy(self)
        new_instance.__dict__["output_hooks"] = hooks
        return new_instance

    def save_wrapper(self, save_func, data: Tout, *args, **kwargs) -> None:
        for hook in self.output_hooks:
            hook.before_output_save(self, data)  # type: ignore[arg-type]

        save_func(data, *args, **kwargs)

        for hook in self.output_hooks:
            hook.after_output_save(self, data)  # type: ignore[arg-type]


class _OutputReferences(_BaseOutput[Tout], Generic[Tout]):
    """Class that adds reference tracking to an Output.
    Used for compartmentalizing reference tracking, no reuse."""

    @cached_property
    def references(self) -> dict[str, list[Input | Output | IO]]:
        """Find all attributes of type Input, Output, or IO on the object.

        Returns:
            a dictionary mapping attribute names to lists of Input, Output,
            or IO
        """
        return _find_references(self.__dict__)


class _OutputException(_BaseOutput[Tout]):
    def save_wrapper(self, save_func, data: Tout, *args, **kwargs) -> None:
        try:
            save_func(data, *args, **kwargs)
        except Exception as exc:
            msg = f"Failed to save {self!s}.\n{exc!s}"
            raise IOException(msg) from exc


class Output(
    _OutputOptions[Tout],
    _OutputHooks[Tout],
    _OutputReferences[Tout],
    _OutputException[Tout],
    Generic[Tout],
    metaclass=_OutputMeta,
):
    """Base class for all outputs in Ordeq. An `Output` is a class that saves
    data. All `Output` classes should implement a save method. By default,
    saving an output does nothing. See the Ordeq IO packages for some
    out-of-the-box implementations (e.g., `YAML`, `StringBuffer`, etc.).

    `Output` can also be used directly as placeholder. This can be useful when
    you are defining a node, but you do not want to provide an actual output.
    In this case, you can:

    ```python
    >>> from ordeq.framework import Output, node
    >>> from ordeq_common import StringBuffer

    >>> greeting = StringBuffer("hello")
    >>> greeting_upper = Output[str]()

    >>> @node(
    ...     inputs=greeting,
    ...     outputs=greeting_upper
    ... )
    ... def uppercase(greeting: str) -> str:
    ...     return greeting.upper()

    ```

    In the example above, `greeting_upper` represents the placeholder output
    to the node `uppercase`. When you run the node `uppercase`, its result can
    be retrieved from the `greeting_upper` output. For instance:

    ```python
    >>> from ordeq import run
    >>> result = run(uppercase)
    >>> result[greeting_upper]
    'HELLO'
    ```
    """

    def __init__(self):
        self._idx = str(uuid4())

    def __repr__(self):
        return f"Output(idx={self._idx})"


class _IOMeta(_InputMeta, _OutputMeta): ...


class IO(Input[T], Output[T], metaclass=_IOMeta):
    """Base class for all IOs in Ordeq. An `IO` is a class that can both load
    and save data. See the Ordeq IO packages for some out-of-the-box
    implementations (e.g., `YAML`, `StringBuffer`, etc.).

    `IO` can also be used directly as placeholder. This can be useful when
    you want to pass data from one node to another, but you do not want to save
    the data in between:

    ```python
    >>> from ordeq import Input, node
    >>> from ordeq_common import StringBuffer, Literal

    >>> hello = StringBuffer("hi")
    >>> name = Literal("Bob")
    >>> greeting = IO[str]()
    >>> greeting_capitalized = StringBuffer()

    >>> @node(
    ...     inputs=[hello, name],
    ...     outputs=greeting
    ... )
    ... def greet(greeting: str, name: str) -> str:
    ...     return f"{greeting}, {name}!"

    >>> @node(
    ...     inputs=greeting,
    ...     outputs=greeting_capitalized
    ... )
    ... def capitalize(s: str) -> str:
    ...     return s.capitalize()
    ```

    In the example above, `greeting` represents the placeholder output
    to the node `greet`, as well as the placeholder input to `capitalize`.

    When you run the nodes `greeting` and `capitalize` the result of `greeting`
    will be passed along unaffected to `capitalize`, much like a cache:

    ```python
    >>> from ordeq import run
    >>> result = run(greet, capitalize)
    >>> result[greeting]
    'hi, Bob!'
    ```
    """

    def __repr__(self):
        return f"IO(idx={self._idx})"
