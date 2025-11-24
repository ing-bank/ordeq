from dataclasses import dataclass
from typing import Any

from ordeq import Output


@dataclass(frozen=True, eq=False)
class Print(Output[Any]):
    """Output that prints data on save. Mostly useful for debugging purposes.
    The difference between other utilities like `StringBuffer` and `Pass` is
    that `Print` shows the output of the node directly on the console.

    Example:

    ```pycon
    >>> from ordeq_common import Print
    >>> from ordeq import node, run, Input
    >>> @node(
    ...     inputs=Input[str]("hello, world!"),
    ...     outputs=Print()
    ... )
    ... def print_message(message: str) -> str:
    ...     return message.capitalize()

    >>> run(print_message)
    Hello, world!

    >>> import sys
    >>> @node(
    ...     inputs=Input[str]("error message"),
    ...     outputs=Print().with_save_options(file=sys.stderr)
    ... )
    ... def log_error(message: str) -> str:
    ...     return f"Error: {message}"

    >>> run(log_error)  # prints to stderr

    ```
    """

    def save(self, data: Any, **save_options: Any) -> None:
        print(data, **save_options)
