from dataclasses import InitVar, dataclass, field
from io import BytesIO

from ordeq import IO


@dataclass(frozen=True, eq=False)
class BytesBuffer(IO[bytes]):
    """IO that uses an in-memory bytes buffer to load and save data. Useful
    for buffering data across nodes without writing to disk.

    Example:

    ```pycon
    >>> from ordeq_common import BytesBuffer
    >>> buffer = BytesBuffer()
    >>> buffer.load()
    b''

    ```

    The buffer is initially empty, unless provided with initial data:

    ```pycon
    >>> buffer = BytesBuffer(b"Initial data")
    >>> buffer.load()
    b'Initial data'

    ```

    Saving to the buffer appends data to the existing content:

    ```pycon
    >>> buffer.save(b"New data")
    >>> buffer.load()
    b'Initial dataNew data'

    ```

    Example in a node:

    ```pycon
    >>> from ordeq_args import CommandLineArg
    >>> from ordeq_common import BytesBuffer, Literal
    >>> from ordeq import node, run
    >>> result = BytesBuffer()
    >>> @node(
    ...     inputs=[BytesBuffer(b"Hello"), Literal(b"you")], outputs=result
    ... )
    ... def greet(greeting: bytes, name: bytes) -> bytes:
    ...     return greeting + b" to " + name + b"!"
    >>> _ = run(greet)
    >>> result.load()
    b'Hello to you!'

    ```

    """

    _buffer: BytesIO = field(default_factory=BytesIO, init=False)
    value: InitVar[bytes | None] = None

    def __post_init__(self, value: bytes | None):
        if value is not None:
            self._buffer.write(value)

    def load(self) -> bytes:
        return self._buffer.getvalue()

    def save(self, data: bytes) -> None:
        self._buffer.write(data)
