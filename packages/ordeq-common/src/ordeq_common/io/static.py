from dataclasses import dataclass
from typing import TypeVar

from ordeq.framework.io import Input

T = TypeVar("T")


@dataclass(frozen=True, eq=False)
class Static(Input[T]):
    """IO that returns a pre-defined value on load. Mostly useful for
    testing purposes.

    Example:

    ```pycon
    >>> from ordeq_common import Static
    >>> Static("someValue").load()
    'someValue'

    ```

    """

    value: T

    def load(self) -> T:
        return self.value
