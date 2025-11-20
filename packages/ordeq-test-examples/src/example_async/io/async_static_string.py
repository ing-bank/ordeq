import asyncio
from dataclasses import dataclass

from ordeq import Input


@dataclass(frozen=True, eq=False)
class AsyncStaticString(Input[str]):
    """Example IO that simulates asynchronous loading of a static string.
    It uses asyncio.sleep to mimic I/O-bound delays.

    In a real-world scenario, this could represent an async read from a
    database, web service, or file system.
    """

    value: str
    sleep_delay: float = 1.0  # seconds

    async def load(self) -> str:
        await asyncio.sleep(self.sleep_delay)  # Simulate async load delay
        return self.value
