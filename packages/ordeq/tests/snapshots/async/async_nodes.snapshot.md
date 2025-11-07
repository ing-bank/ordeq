## Resource

```python
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

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("StringBuffer")]:::io0
		end
	end

	write_buffer_2 --> IO0
	write_buffer_1 --> IO1

	subgraph pipeline["Pipeline"]
		direction TB
		write_buffer_2(["write_buffer_2"]):::node
		write_buffer_1(["write_buffer_1"]):::node
		IO0[("buffer_2")]:::io0
		IO1[("buffer_1")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

edges:  {Node(name=example_async.async_nodes:write_buffer_1_sync, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [], Node(name=example_async.async_nodes:write_buffer_2_sync, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]): []}
Running sync node Node(name=example_async.async_nodes:write_buffer_1_sync, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
Start fetching buffer_1...
Finished fetching buffer_1 after 4 seconds.
Running sync node Node(name=example_async.async_nodes:write_buffer_2_sync, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
Start analyzing buffer_2...
Finished analyzing buffer_2 after 2 seconds.
Total elapsed time: 6.011369 seconds

```

## Logging

```text
INFO	ordeq.runner	Running node "write_buffer_1_sync" in module "example_async.async_nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "write_buffer_2_sync" in module "example_async.async_nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```