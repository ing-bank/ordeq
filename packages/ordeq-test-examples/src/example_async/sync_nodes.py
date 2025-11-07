"""Non-async nodes with simulated delays to demonstrate synchronous execution
compared to async nodes.

In this example, both nodes use time.sleep to simulate I/O-bound operations.
The execution in total should take approximately the sum of the durations
of all nodes (6 seconds).
"""

import time

from ordeq import node
from ordeq_common import StringBuffer

buffer_1 = StringBuffer()
buffer_2 = StringBuffer()


@node(outputs=[buffer_1])
def write_buffer_1() -> str:
    name = "buffer_1"
    delay = 4
    print(f"Start fetching {name}...")
    time.sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds.")
    return f"{name} data"


@node(outputs=[buffer_2])
def write_buffer_2() -> str:
    name = "buffer_2"
    delay = 2
    print(f"Start analyzing {name}...")
    time.sleep(delay)
    print(f"Finished analyzing {name} after {delay} seconds.")
    return f"{name} data"
