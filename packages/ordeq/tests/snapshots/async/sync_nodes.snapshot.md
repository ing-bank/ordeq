## Resource

```python
from example_async import sync_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(sync_nodes, fmt="mermaid"))
run(sync_nodes)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "StringBuffer"}
	end

	example_async.sync_nodes:write_buffer_1 --> example_async.sync_nodes:buffer_1
	example_async.sync_nodes:write_buffer_2 --> example_async.sync_nodes:buffer_2

	example_async.sync_nodes:write_buffer_1@{shape: rounded, label: "write_buffer_1"}
	example_async.sync_nodes:write_buffer_2@{shape: rounded, label: "write_buffer_2"}
	example_async.sync_nodes:buffer_1@{shape: rect, label: "buffer_1"}
	example_async.sync_nodes:buffer_2@{shape: rect, label: "buffer_2"}

	class L0,example_async.sync_nodes:write_buffer_1,example_async.sync_nodes:write_buffer_2 node
	class L00,example_async.sync_nodes:buffer_1,example_async.sync_nodes:buffer_2 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

Start fetching buffer_1...
Finished fetching buffer_1 after 4 seconds.
Start analyzing buffer_2...
Finished analyzing buffer_2 after 2 seconds.

```

## Logging

```text
INFO	ordeq.runner	Running node 'write_buffer_1' in module 'example_async.sync_nodes'
INFO	ordeq.io	Saving 'buffer_1' in module 'example_async.sync_nodes'
DEBUG	ordeq.io	Persisting data for 'buffer_1' in module 'example_async.sync_nodes'
INFO	ordeq.runner	Running node 'write_buffer_2' in module 'example_async.sync_nodes'
INFO	ordeq.io	Saving 'buffer_2' in module 'example_async.sync_nodes'
DEBUG	ordeq.io	Persisting data for 'buffer_2' in module 'example_async.sync_nodes'
DEBUG	ordeq.io	Unpersisting data for 'buffer_2' in module 'example_async.sync_nodes'
DEBUG	ordeq.io	Unpersisting data for 'buffer_1' in module 'example_async.sync_nodes'

```