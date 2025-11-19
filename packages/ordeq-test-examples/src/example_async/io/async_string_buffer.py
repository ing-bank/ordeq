import asyncio
from dataclasses import InitVar, dataclass, field
from io import StringIO

from ordeq import IO


@dataclass(frozen=True, eq=False)
class AsyncStringBuffer(IO[str]):
    """Example IO that simulates asynchronous loading of a string buffer.
    It uses asyncio.sleep to mimic I/O-bound delays.

    In a real-world scenario, this could represent an async read from a
    database, web service, or file system.
    """

    _buffer: StringIO = field(default_factory=StringIO, init=False)
    value: InitVar[str | None] = None
    sleep_delay: float = 1.0  # seconds

    async def load(self) -> str:
        await asyncio.sleep(self.sleep_delay)  # Simulate async load delay
        return self._buffer.getvalue()

    async def save(self, data: str) -> None:
        await asyncio.sleep(self.sleep_delay)  # Simulate async save delay
        self._buffer.write(data)

    def persist(self, _) -> None:
        return super().persist(self._buffer.getvalue())
