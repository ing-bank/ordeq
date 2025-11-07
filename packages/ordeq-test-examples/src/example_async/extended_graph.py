"""This example demonstrates an extended asynchronous graph using ordeq.

Multiple async nodes with varying execution times are defined, showcasing
concurrent execution. The final node is synchronous, illustrating
the integration of async and sync nodes within the same graph.

In the example below we have several async nodes running in different
branches of the graph. Nodes A and B run concurrently, followed by
node C which depends on both. Simultaneously, nodes D and E run,
followed by node F which depends on both. Finally, node G combines
the results of nodes C and F.
"""

import asyncio

from ordeq import node
from ordeq_common import StringBuffer

A = StringBuffer()
B = StringBuffer()
C = StringBuffer()
D = StringBuffer()
E = StringBuffer()
F = StringBuffer()
G = StringBuffer()

processed_buffer = StringBuffer()

VERY_SLOW_EXEC_TIME = 6
SLOW_EXEC_TIME = 4
FAST_EXEC_TIME = 2


@node(outputs=[A])
async def write_A() -> str:
    name = "A"
    delay = SLOW_EXEC_TIME
    print(f"Start fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds.")
    return f"{name} data"


@node(outputs=[B])
async def write_B() -> str:
    name = "B"
    delay = SLOW_EXEC_TIME
    print(f"Start analyzing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished analyzing {name} after {delay} seconds.")
    return f"{name} data"


@node(inputs=[A, B], outputs=[C])
async def write_C(a: str, b: str) -> str:
    name = "C"
    delay = FAST_EXEC_TIME
    print(f"Start processing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished processing {name} after {delay} seconds.")
    return f"{a}, {b}, {name} data"


@node(outputs=[D])
async def write_D() -> str:
    name = "D"
    delay = FAST_EXEC_TIME
    print(f"Start processing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished processing {name} after {delay} seconds.")
    return f"{name} data"


@node(outputs=[E])
async def write_E() -> str:
    name = "E"
    delay = FAST_EXEC_TIME
    print(f"Start processing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished processing {name} after {delay} seconds.")
    return f"{name} data"


@node(inputs=[D, E], outputs=[F])
async def write_F(d: str, e: str) -> str:
    name = "F"
    delay = VERY_SLOW_EXEC_TIME
    print(f"Start processing {name}...")
    await asyncio.sleep(delay)
    print(f"Finished processing {name} after {delay} seconds.")
    return f"{d}, {e}, {name} data"


@node(inputs=[C, F], outputs=[G])
def write_G(c: str, f: str) -> str:
    name = "G"
    print(f"Start processing {name}...")
    return f"{c}, {f}, {name} data"
