"""Example Async IO ordeq implementations

Demonstrates how to create custom asynchronous IO classes using ordeq.

In the example below, we define AsyncStaticString, which simulates
asynchronous loading of static strings with different delays.

This example showcases how async IO can be integrated into an
ordeq workflow, allowing nodes to process data as it becomes available,
rather than waiting for all data to be ready.

The execution in total should take approximately the duration
of the longest individual async IO load (3 seconds), rather than
the sum of all durations (5 seconds) as would be the case
with synchronous execution.
"""

import asyncio
from dataclasses import dataclass

from ordeq import Input, node
from ordeq_common.io.string_buffer import StringBuffer


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


slow_string_io = AsyncStaticString(
    value="This string was loaded slowly.", sleep_delay=3.0
)
fast_string_io = AsyncStaticString(
    value="This string was loaded quickly!", sleep_delay=2.0
)
fast_result = StringBuffer()
slow_result = StringBuffer()
combined_result = StringBuffer()


@node(inputs=[slow_string_io], outputs=[slow_result])
def process_slow_string(data: str) -> str:
    return f"Result of slow data: {data}"


@node(inputs=[fast_string_io], outputs=[fast_result])
def process_fast_string(data: str) -> str:
    return f"Result of fast data: {data}"


@node(inputs=[slow_result, fast_result], outputs=[combined_result])
def combine_results(slow: str, fast: str) -> str:
    return f"Combined Results:\n{slow}\n{fast}"
