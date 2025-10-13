from dataclasses import InitVar, dataclass, field
from io import StringIO

from ordeq import IO


@dataclass(frozen=True, eq=False)
class StringBuffer(IO[str]):
    """IO that uses an in-memory string buffer to load and save data. Useful
    for buffering data across nodes without writing to disk.

    Example:

    ```pycon
    >>> from ordeq_common import StringBuffer
    >>> buffer = StringBuffer()
    >>> buffer.load()
    ''

    ```

    The buffer is initially empty, unless provided with initial data:

    ```pycon
    >>> buffer = StringBuffer("Initial data")
    >>> buffer.load()
    'Initial data'

    ```

    Saving to the buffer appends data to the existing content:

    ```pycon
    >>> buffer.save("New data")
    >>> buffer.load()
    'Initial dataNew data'

    ```

    Example in a node:

    ```pycon
    >>> from ordeq_args import CommandLineArg
    >>> from ordeq_common import StringBuffer, Literal
    >>> from ordeq import node, run
    >>> result = StringBuffer("Greeting")
    >>> @node(
    ...     inputs=[StringBuffer("Hello"), Literal("you")],
    ...     outputs=result
    ... )
    ... def greet(greeting: str, name: str) -> str:
    ...     return f"{greeting}, {name}!"
    >>> run(greet).get(result)
    'Hello, you!'

    ```

    """

    _buffer: StringIO = field(default_factory=StringIO, init=False)
    value: InitVar[str | None] = None

    def __post_init__(self, value: str | None):
        if value is not None:
            self._buffer.write(value)

    def load(self) -> str:
        return self._buffer.getvalue()

    def save(self, data: str) -> None:
        self._buffer.write(data)
