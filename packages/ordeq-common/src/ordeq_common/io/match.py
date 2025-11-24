from dataclasses import dataclass, replace
from typing import Generic, TypeVar, overload

from ordeq import Input, Output

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

T = TypeVar("T")
Tkey = TypeVar("Tkey")
Tval = TypeVar("Tval")


@dataclass(frozen=True, kw_only=True)
class MatchOnLoad(Input[Tval], Generic[Tkey, Tval]):
    io: Input[Tkey]
    cases: tuple[tuple[Tkey, Input[Tval]], ...] = ()
    default: Input[Tval] | None = None

    def _match(self, value: Tkey) -> Input[Tval]:
        for case, io in self.cases:
            if value == case:
                return io
        if self.default is not None:
            return self.default
        raise TypeError(f"Unsupported case '{value}'")

    def load(self) -> Tval:
        return self._match(self.io.load()).load()

    def Case(self, key: Tkey, val: Input[Tval]) -> Self:
        return replace(self, cases=(*self.cases, (key, val)))

    def Default(self, val: Input[Tval]) -> Self:
        return replace(self, default=val)


@dataclass(frozen=True, kw_only=True)
class MatchOnSave(Output[tuple[Tkey, Tval]], Generic[Tkey, Tval]):
    cases: tuple[tuple[Tkey, Output[Tval]], ...] = ()
    default: Output[Tval] | None = None

    def _match(self, value: Tkey) -> Output[Tval]:
        for case, io in self.cases:
            if value == case:
                return io
        if self.default is not None:
            return self.default
        raise TypeError(f"Unsupported case '{value}'")

    def save(self, data: tuple[Tkey, Tval]) -> None:
        key, value = data
        self._match(key).save(value)

    def Case(self, key: Tkey, val: Output[Tval]) -> Self:
        return replace(self, cases=(*self.cases, (key, val)))

    def Default(self, val: Output[Tval]) -> Self:
        return replace(self, default=val)


@overload
def Match(io: Input[Tkey]) -> MatchOnLoad[Tval, Tkey]: ...


@overload
def Match() -> MatchOnSave[Tval, Tkey]: ...


def Match(io: Input[Tkey] | None = None) -> MatchOnLoad | MatchOnSave:
    """Utility IO that allows dynamic switching between IO, like the match-case
    statement in Python.

    Example:

    ```pycon
    >>> from ordeq import Input
    >>> from ordeq_common import Match
    >>> from ordeq_args import EnvironmentVariable
    >>> import os
    >>> Country = (
    ...     Match(EnvironmentVariable("COUNTRY"))
    ...     .Case("NL", Input("Netherlands"))
    ...     .Case("BE", Input("Belgium"))
    ...     .Default(Input("Unknown"))
    ... )
    >>> os.environ["COUNTRY"] = "NL"
    >>> Country.load()
    'Netherlands'

    ```

    If a default is provided, it will be used when no cases match:

    ```pycon
    >>> os.environ["COUNTRY"] = "DE"
    >>> Country.load()
    'Unknown'

    ```

    Otherwise, it raises an error when none of the provided cases are matched:

    ```pycon
    >>> Match(EnvironmentVariable("COUNTRY")).load()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ordeq.IOException: Failed to load
    Unsupported case 'DE'
    ```

    Match on save works as follows:

    ```pycon
    >>> SmallOrLarge = (
    ...     Match()
    ...     .Case("S", EnvironmentVariable("SMALL"))
    ...     .Case("L", EnvironmentVariable("LARGE"))
    ...     .Default(EnvironmentVariable("UNKNOWN"))
    ... )
    >>> SmallOrLarge.save(("S", "Andorra"))
    >>> SmallOrLarge.save(("L", "Russia"))
    >>> SmallOrLarge.save(("XXL", "Mars"))
    >>> os.environ["SMALL"]
    'Andorra'
    >>> os.environ.get("LARGE")
    'Russia'
    >>> os.environ.get("UNKNOWN")
    'Mars'

    ```

    Example in a node:

    ```pycon
    >>> from ordeq import node
    >>> from ordeq_files import JSON
    >>> from ordeq_args import CommandLineArg
    >>> from pathlib import Path
    >>> TestOrTrain = (
    ...     Match(CommandLineArg("--split"))
    ...     .Case("test", JSON(path=Path("to/test.json")))
    ...     .Case("train", JSON(path=Path("to/train.json")))
    ... )
    >>> @node(
    ...     inputs=TestOrTrain,
    ... )
    ... def evaluate(data: dict) -> dict:
    ...     ...

    ```

    Returns:
        MatchOnLoad or MatchOnSave
    """  # noqa: E501 (line too long)

    if io is None:
        return MatchOnSave()
    return MatchOnLoad(io=io)
