import asyncio
from pathlib import Path
from time import sleep, time_ns

from ordeq import node, run
from ordeq_common import StringBuffer
from ordeq_viz import viz

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
