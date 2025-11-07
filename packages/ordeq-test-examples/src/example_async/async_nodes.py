"""Async nodes example using ordeq.

Demonstrates the use of asynchronous nodes with simulated
delays of I/O-bound operations with asyncio.sleep.

In the example below, write_buffer_2 should complete before
write_buffer_1, despite being started after it, due to
the shorter delay.

The execution in total should take approximately the duration
of the longest individual async node (4 seconds), rather than
the sum of all durations (6 seconds) as would be the case
with synchronous execution.
"""

import asyncio

from ordeq import node
from ordeq_common import StringBuffer

buffer_1 = StringBuffer()
buffer_2 = StringBuffer()


@node(outputs=[buffer_1])
async def write_buffer_1() -> str:
    name = "buffer_1"
    delay = 4
    print(f"Start fetching {name}...")
    # Simulate async I/O delay,
    # This should free up event loop for other async nodes
    await asyncio.sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds.")
    return f"{name} data"


@node(outputs=[buffer_2])
async def write_buffer_2() -> str:
    name = "buffer_2"
    delay = 2
    print(f"Start analyzing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished analyzing {name} after {delay} seconds.")
    return f"{name} data"
