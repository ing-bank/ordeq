"""Example of mixed async and sync nodes using ordeq.
Demonstrates async nodes producing data for a sync node to process.
The async nodes simulate I/O-bound operations with asyncio.sleep.
The sync node processes the results of the async nodes without delays.

In this example, write_buffer_1 and write_buffer_2 should run concurrently,
with write_buffer_2 finishing first due to the shorter delay.
The process_buffer node then processes the result of write_buffer_2 once
it's finished.
"""

import asyncio

from ordeq import node
from ordeq_common import StringBuffer

buffer_1 = StringBuffer()
buffer_2 = StringBuffer()

processed_buffer = StringBuffer()


@node(outputs=[buffer_1])
async def write_buffer_1() -> str:
    name = "buffer_1"
    delay = 4
    print(f"Start fetching {name}...")
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


@node(inputs=[buffer_2], outputs=[processed_buffer])
def process_buffer(buf1: str) -> str:
    name = "processed_buffer"
    print(f"Start processing {name}...")
    result = f"Processed ({buf1}) into {name}."
    print(f"Finished processing {name}.")
    return result
