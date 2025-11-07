import asyncio
from pathlib import Path
from time import sleep, time_ns

from example_async.async_nodes import async_nodes, sync_nodes
from ordeq import run
from ordeq_common import StringBuffer
from ordeq_viz import viz

diagram = viz(
    *async_nodes, fmt="mermaid", output=Path("tmp/async_pipeline.mermaid")
)
print(diagram)
start_time = time_ns()
# run(*async_nodes, run_async=True)
run(*sync_nodes, run_async=False)
end_time = time_ns()
elapsed_time = (end_time - start_time) / 1_000_000_000
print(f"Total elapsed time: {elapsed_time} seconds")
