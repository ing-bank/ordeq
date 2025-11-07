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


@node(inputs=[buffer_2], outputs=[processed_buffer])
def process_buffer(data: str) -> None:
    print(f"Processing data: {data}")
    return f"processed {data}"


@node(outputs=[buffer_1])
def write_buffer_1_sync() -> str:
    name = "buffer_1"
    delay = 4
    print(f"Start fetching {name}...")
    sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds.")
    return f"{name} data"


@node(outputs=[buffer_2])
def write_buffer_2_sync() -> str:
    name = "buffer_2"
    delay = 2
    print(f"Start analyzing {name}...")
    sleep(delay)
    print(f"Finished analyzing {name} after {delay} seconds.")
    return f"{name} data"


# async_nodes = [write_buffer_1, write_buffer_2, process_buffer]
async_nodes = [write_buffer_1, write_buffer_2]
sync_nodes = [write_buffer_1_sync, write_buffer_2_sync, process_buffer]
sync_nodes = [write_buffer_1_sync, write_buffer_2_sync]
