from dataclasses import dataclass
from typing import Any

from ordeq.framework.io import Output


@dataclass(frozen=True, eq=False)
class Print(Output[Any]):
    """Output that prints data on save. Mostly useful for debugging purposes.
    The difference between other utilities like `StringBuffer` and `Pass` is
    that `Print` shows the output of the node directly on the console.

    Example:

    ```pycon
    >>> from ordeq_common import Print, Literal
    >>> from ordeq import node, run
    >>> @node(
    ...     inputs=Literal("hello, world!"),
    ...     outputs=Print()
    ... )
    ... def print_message(message: str) -> str:
    ...     return message.capitalize()

    >>> result = run(print_message)
    Hello, world!

    ```

    """

    def save(self, data: Any) -> None:
        print(data)
