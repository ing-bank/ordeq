from __future__ import annotations

import inspect
import logging
import warnings
from collections.abc import Callable, Hashable, Sequence
from copy import copy
from functools import cached_property, reduce, wraps
from typing import (
    Annotated,
    Any,
    Generic,
    TypeAlias,
    TypeGuard,
    TypeVar,
    final,
)

from ordeq.preview import preview

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

from ordeq._fqn import FQN
from ordeq._hook import InputHook, OutputHook

logger = logging.getLogger("ordeq.io")


class IOException(Exception):
    """Exception raised by IO implementations in case of load/save failure.
    IO implementations should provide instructive information.
    """


T = TypeVar("T")
Tin = TypeVar("Tin")
Tout = TypeVar("Tout")


def _is_io(obj: object) -> TypeGuard[AnyIO]:
    return isinstance(obj, (IO, Input, Output))


def _resolve_sequence_to_ios(value: Any) -> list[AnyIO]:
    if _is_io(value):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [io for v in value for io in _resolve_sequence_to_ios(v)]
    if isinstance(value, dict):
        return [
            io for v in value.values() for io in _resolve_sequence_to_ios(v)
        ]
    return []


def _is_io_sequence(value: Any) -> bool:
    return bool(_resolve_sequence_to_ios(value))


def _find_references(attributes) -> dict[str, list[AnyIO]]:
    """Find all attributes of type Input, Output, or IO.

    Args:
        attributes: a dictionary of attributes to inspect

    Returns:
        a dictionary mapping attribute names to lists of Input, Output, or IO
    """
    wrapped = {}
    for attribute, value in attributes.items():
        ios = _resolve_sequence_to_ios(value)
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

        try:
            return composed(*args, **kwargs)
        except Exception as exc:
            msg = f"Failed to load {self!s}.\n{exc!s}"
            raise IOException(msg) from exc

    return wrapper


def _warn_if_eq_or_hash_is_implemented(name, class_dict):
    for method in "__eq__", "__hash__":
        if "__hash__" in class_dict:
            warnings.warn(
                f"IO {name} implements '{method}'. This will be ignored.",
                stacklevel=2,
            )


def _process_input_meta(name, bases, class_dict):
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
                and param.kind != inspect._ParameterKind.VAR_KEYWORD
            ):
                raise TypeError(
                    f"Argument '{argument}' of function "
                    f"'{load_method.__name__}' has no default value."
                )

    if not hasattr(load_method, "__wrapped__"):
        class_dict["load"] = _load_decorator(load_method)
    return class_dict, bases


def _pass(*args, **kwargs):
    return


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

        try:
            composed(data, *args, **kwargs)
        except Exception as exc:
            msg = f"Failed to save {self!s}.\n{exc!s}"
            raise IOException(msg) from exc

    return wrapper


def _process_output_meta(name, bases, class_dict):
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
        seen_data = False
        for argument, param in sig.parameters.items():
            if argument in {"self", "cls"}:
                continue

            if not seen_data:
                seen_data = True
                continue  # Skip the data parameter itself

            # Ensure all arguments (except the first two, self/cls and data)
            # have default values
            if (
                param.default is inspect.Parameter.empty
                and param.kind != inspect._ParameterKind.VAR_KEYWORD
            ):
                raise TypeError(
                    f"Argument '{argument}' of function "
                    f"'{save_method.__name__}' has no default value."
                )

        if not seen_data:
            raise TypeError("Save method requires a data parameter.")

        if (
            sig.return_annotation != inspect.Signature.empty
            and sig.return_annotation is not None
        ):
            raise TypeError("Save method must have return type None.")

        if not hasattr(save_method, "__wrapped__"):
            class_dict["save"] = _save_decorator(save_method)
    return class_dict, bases


def _has_base(bases, target_names: set[str]) -> bool:
    def _check_ancestor(cls) -> bool:
        if cls.__name__ in target_names:
            return True

        # Recursively check all ancestors in MRO
        for ancestor in getattr(cls, "__mro__", [])[
            1:
        ]:  # Skip self (first element)
            if ancestor.__name__ in target_names:
                return True

            if (
                hasattr(ancestor, "__bases__")
                and ancestor.__bases__
                and _has_base(ancestor.__bases__, target_names)
            ):
                return True
        return False

    return any(_check_ancestor(base) for base in bases)


def eq(self, other) -> bool:
    return id(self) == id(other)


def h(self) -> int:
    return id(self)


class _WithEq:
    """
    Interface defining the default equality and hashing behavior for IO
    objects based on their identity. This ensures that each IO instance is
    treated as unique, regardless of its internal state or attributes.

    If the __eq__ and __hash__ methods are explicitly overridden in the
    subclass, a type error will be raised.
    """

    @final
    def __eq__(self, other) -> bool:
        return id(self) == id(other)

    @final
    def __hash__(self) -> int:
        return id(self)


class _IOMeta(type):
    """Metaclass that handles Input and Output logic."""

    def __new__(cls, name, bases, class_dict):
        # Check if this class inherits from Input or Output
        has_input_base = _has_base(bases, {"Input", "IO"})
        has_output_base = _has_base(bases, {"Output", "IO"})

        # Apply input metaclass logic if needed
        if has_input_base or name in {"Input", "IO"}:
            class_dict, bases = _process_input_meta(name, bases, class_dict)

        # Apply output metaclass logic if needed
        if has_output_base or name in {"Output", "IO"}:
            class_dict, bases = _process_output_meta(name, bases, class_dict)

        _warn_if_eq_or_hash_is_implemented(name, class_dict)

        return super().__new__(cls, name, bases, class_dict)

    def __init__(cls, name, bases, class_dict):
        if name not in {"Input", "Output", "IO"}:
            # Each IO instance is unique, so we override __eq__ and __hash__
            # to ensure identity-based comparison and hashing.
            cls.__eq__ = _WithEq.__eq__  # type: ignore[invalid-assignment,method-assign,assignment]
            cls.__hash__ = _WithEq.__hash__  # type: ignore[invalid-assignment,method-assign,assignment]
        super().__init__(name, bases, class_dict)


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

        new_instance = copy(self)

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

        new_instance = copy(self)
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
    def references(self) -> dict[str, list[AnyIO]]:
        """Find all attributes of type Input, Output, or IO on the object.

        Returns:
            a dictionary mapping attribute names to lists of Input, Output,
            or IO
        """
        return _find_references(self.__dict__)


class _InputCache(_BaseInput[Tin]):
    """Class that adds caching to an Input."""

    _data: Tin
    _unpersist: bool = True

    def __init__(self, value: Any = None):
        super().__init__()
        if type(self).__name__ in {"Input", "IO"} and value is not None:
            self.persist(value)
            self.retain()

    @property
    def is_persisted(self) -> bool:
        return hasattr(self, "_data")

    def load_wrapper(self, load_func, *args, **kwargs) -> Tin:
        if not self.is_persisted:
            return load_func(*args, **kwargs)
        logger.debug("Loading cached data for %s", self)
        return self._data

    def persist(self, data: Tin) -> None:
        logger.debug("Persisting data for %s", self)
        self.__dict__["_data"] = data

    def retain(self) -> Self:
        self._unpersist = False
        return self

    def unpersist(self) -> None:
        if not self._unpersist:
            return
        if self.is_persisted:
            logger.debug("Unpersisting data for %s", self)
            del self.__dict__["_data"]


class _WithAttributes:
    _attributes: dict[str, Any] | None = None

    def with_attributes(self, **attributes) -> Self:
        new_instance = copy(self)
        new_instance.__dict__["_attributes"] = attributes
        return new_instance


class _WithTypeFQN:
    @property
    def type_fqn(self) -> FQN:
        t = type(self)
        return FQN(t.__module__, t.__name__)


class _WithName(_WithTypeFQN):
    _module: str | None = None
    _name: str | None = None

    @property
    def fqn(self) -> FQN | None:
        if self.is_fq:
            return FQN(module=self._module, name=self._name)  # type: ignore[arg-type]
        return None

    def _set_fqn(self, fqn: FQN) -> None:
        self.__dict__["_module"] = fqn.module
        self.__dict__["_name"] = fqn.name

    def _set_name(self, name: str) -> None:
        self.__dict__["_name"] = name

    @property
    def is_fq(self) -> bool:
        return self._module is not None and self._name is not None

    def __str__(self) -> str:
        if self.is_fq:
            return f"{self.type_fqn.name} {self.fqn:desc}"
        return repr(self)


ResourceType: TypeAlias = Annotated[
    Hashable,
    """Any hashable object that is used to identify an IO resource.
    Examples: pathlib.Path, str.""",
]


class _WithResource:
    _resource_: ResourceType = None

    def with_resource(self, resource: ResourceType) -> Self:
        if resource is None:
            raise ValueError("Resource cannot be None.")
        preview(
            "Resources are in preview mode and may change "
            "without notice in future releases."
        )
        new_instance = copy(self)
        new_instance.__dict__["_resource_"] = resource
        return new_instance

    @property
    def _resource(self) -> ResourceType:
        return self._resource_ or self

    def __matmul__(self, resource: ResourceType) -> Self:
        return self.with_resource(resource)


class Input(
    _InputOptions[Tin],
    _InputHooks[Tin],
    _InputReferences[Tin],
    _InputCache[Tin],
    _WithResource,
    _WithName,
    _WithAttributes,
    _WithEq,
    Generic[Tin],
    metaclass=_IOMeta,
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
    >>> from ordeq import Input, node
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
    >>> from ordeq import Input
    >>> run(greet, io={name: Input[str]("Alice")})
    >>> greeting.load()
    'Hello, Alice!'
    ```
    """

    def __repr__(self):
        return f"Input(id={id(self)})"


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

        new_instance = copy(self)

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

        new_instance = copy(self)
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
    def references(self) -> dict[str, list[AnyIO]]:
        """Find all attributes of type Input, Output, or IO on the object.

        Returns:
            a dictionary mapping attribute names to lists of Input, Output,
            or IO
        """
        return _find_references(self.__dict__)


class Output(
    _OutputOptions[Tout],
    _OutputHooks[Tout],
    _OutputReferences[Tout],
    _WithResource,
    _WithName,
    _WithAttributes,
    _WithEq,
    Generic[Tout],
    metaclass=_IOMeta,
):
    """Base class for all outputs in Ordeq. An `Output` is a class that saves
    data. All `Output` classes should implement a save method. By default,
    saving an output does nothing. See the Ordeq IO packages for some
    out-of-the-box implementations (e.g., `YAML`, `StringBuffer`, etc.).

    `Output` can also be used directly as placeholder. This can be useful when
    you are defining a node, but you do not want to provide an actual output.
    In this case, you can:

    ```python
    >>> from ordeq import Output, node
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
    >>> run(uppercase)
    >>> greeting_upper.load()
    'HELLO'
    ```
    """

    def __repr__(self):
        return f"Output(id={id(self)})"


class IO(Input[T], Output[T]):
    """Base class for all IOs in Ordeq. An `IO` is a class that can both load
    and save data. See the Ordeq IO packages for some out-of-the-box
    implementations (e.g., `YAML`, `StringBuffer`, etc.).

    `IO` can also be used directly as placeholder. This can be useful when
    you want to pass data from one node to another, but you do not want to save
    the data in between:

    ```python
    >>> from ordeq import Input, node
    >>> from ordeq_common import StringBuffer

    >>> hello = StringBuffer("hi")
    >>> name = Input[str]("Bob")
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
    >>> run(greet, capitalize)
    >>> greeting.load()
    'hi, Bob!'
    ```
    """

    def __repr__(self):
        return f"IO(id={id(self)})"


# Type aliases
AnyIO: TypeAlias = Input[T] | Output[T]


def _is_input(obj: object) -> TypeGuard[Input]:
    return isinstance(obj, Input)


def _is_output(obj: object) -> TypeGuard[Output]:
    return isinstance(obj, Output)
