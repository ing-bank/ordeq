"""Example of ordeq run using both Async IOs and Async Nodes.

This example demonstrates the use of asynchronous IOs and nodes
within the same graph.

In the example below, two async IOs simulate data retrieval with
different delays. An async node retrieves data from each IO,
and a synchronous node processes the combined results.

The async IOs simulate I/O-bound delays using asyncio.sleep, this could
represent something like a network call or database query in a
real-world scenario.

Similarly, the async nodes use asyncio.sleep to mimic processing delays which
could also represent I/O-bound operations like calling an API.

The execution in total should take approximately 8 seconds, which is the sum of
the longest async IO save of the retrieved data (5 seconds) and the time
taken by the sync node to load and save the combined result (3 seconds).
In a synchronous execution model, this would take 12 seconds, as each step
would block the next from starting until it completed.
"""

import asyncio

from ordeq import node

from example_async.io import AsyncStringBuffer

buffer_1 = AsyncStringBuffer(sleep_delay=1.0)
buffer_2 = AsyncStringBuffer(sleep_delay=2.0)
buffer_3 = AsyncStringBuffer(sleep_delay=1.0)


@node(outputs=[buffer_1])  # total time to save: 5 seconds
async def retrieve_data_1() -> str:
    print("Starting retrieval of data 1...")
    await asyncio.sleep(
        4.0
    )  # Simulate async I/O delay, this could be a network call
    print("Completed retrieval of data 1.")
    return "Data from buffer 1"


@node(outputs=[buffer_2])  # total time to save: 3 seconds
async def retrieve_data_2() -> str:
    print("Starting retrieval of data 2...")
    await asyncio.sleep(
        1.0
    )  # Simulate async I/O delay, this could be a network call
    print("Completed retrieval of data 2.")
    return "Data from buffer 2"


@node(
    inputs=[buffer_1, buffer_2], outputs=[buffer_3]
)  # total time to save: 3 seconds (longest input load + output save time)
def process_data(data1: str, data2: str) -> str:
    combined = f"Combined Data:\n{data1}\n{data2}"
    print(combined)
    return combined
