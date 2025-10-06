from dataclasses import dataclass
from typing import TypeVar

from ordeq.framework.io import Input

T = TypeVar("T")


@dataclass(frozen=True, eq=False)
class Literal(Input[T]):
    """IO that returns a pre-defined value on load. Mostly useful for
    testing purposes.

    Example:

    ```pycon
    >>> from ordeq_common import Literal
    >>> value = Literal("someValue")
    >>> value.load()
    'someValue'
    >>> print(value)
    Literal('someValue')

    ```

    """

    value: T

    def load(self) -> T:
        return self.value

    def __repr__(self):
        return f"Literal({self.value!r})"
