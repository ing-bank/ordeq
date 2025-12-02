## Resource

```python
from example_async import async_ios_and_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(async_ios_and_nodes, fmt="mermaid"))
print("Expect retrieve_data_2 node to complete before retrieve_data_1")
run(async_ios_and_nodes)
print(async_ios_and_nodes.buffer_3.load())

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "AsyncStringBuffer"}
		io_type_1@{shape: rect, label: "IO"}
	end

	example_async.async_ios_and_nodes:buffer_1 --> example_async.async_ios_and_nodes:process_data:data1
	example_async.async_ios_and_nodes:buffer_2 --> example_async.async_ios_and_nodes:process_data:data2
	example_async.async_ios_and_nodes:retrieve_data_1 --> example_async.async_ios_and_nodes:buffer_1
	example_async.async_ios_and_nodes:retrieve_data_2 --> example_async.async_ios_and_nodes:buffer_2
	example_async.async_ios_and_nodes:process_data:data1 --> example_async.async_ios_and_nodes:process_data
	example_async.async_ios_and_nodes:process_data:data2 --> example_async.async_ios_and_nodes:process_data
	example_async.async_ios_and_nodes:process_data --> example_async.async_ios_and_nodes:buffer_3

	example_async.async_ios_and_nodes:buffer_1@{shape: rounded, label: "buffer_1"}
	example_async.async_ios_and_nodes:buffer_2@{shape: rounded, label: "buffer_2"}
	example_async.async_ios_and_nodes:retrieve_data_1@{shape: rounded, label: "retrieve_data_1"}
	example_async.async_ios_and_nodes:retrieve_data_2@{shape: rounded, label: "retrieve_data_2"}
	example_async.async_ios_and_nodes:process_data@{shape: rounded, label: "process_data"}
	example_async.async_ios_and_nodes:process_data:data1@{shape: rect, label: "process_data:data1"}
	example_async.async_ios_and_nodes:process_data:data2@{shape: rect, label: "process_data:data2"}
	example_async.async_ios_and_nodes:buffer_1@{shape: rect, label: "buffer_1"}
	example_async.async_ios_and_nodes:buffer_2@{shape: rect, label: "buffer_2"}
	example_async.async_ios_and_nodes:buffer_3@{shape: rect, label: "buffer_3"}

	class node_type,example_async.async_ios_and_nodes:buffer_1,example_async.async_ios_and_nodes:buffer_2,example_async.async_ios_and_nodes:retrieve_data_1,example_async.async_ios_and_nodes:retrieve_data_2,example_async.async_ios_and_nodes:process_data node
	class io_type_0,example_async.async_ios_and_nodes:buffer_1,example_async.async_ios_and_nodes:buffer_2,example_async.async_ios_and_nodes:buffer_3 io0
	class io_type_1,example_async.async_ios_and_nodes:process_data:data1,example_async.async_ios_and_nodes:process_data:data2 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

Expect retrieve_data_2 node to complete before retrieve_data_1
Combined Data:
<coroutine object AsyncStringBuffer.load at HASH1>
<coroutine object AsyncStringBuffer.load at HASH2>
<coroutine object AsyncStringBuffer.load at HASH3>

```

## Warnings

```text
RuntimeWarning: coroutine 'AsyncStringBuffer.save' was never awaited
RuntimeWarning: coroutine 'retrieve_data_2' was never awaited
RuntimeWarning: coroutine 'AsyncStringBuffer.load' was never awaited
RuntimeWarning: coroutine 'AsyncStringBuffer.load' was never awaited
```

## Logging

```text
DEBUG	ordeq.runner	Running AsyncStringBuffer 'buffer_1' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Loading AsyncStringBuffer 'buffer_1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Persisting data for IO 'process_data:data1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.runner	Running AsyncStringBuffer 'buffer_2' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Loading AsyncStringBuffer 'buffer_2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Persisting data for IO 'process_data:data2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.runner	Running node 'retrieve_data_1' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Saving AsyncStringBuffer 'buffer_1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Persisting data for AsyncStringBuffer 'buffer_1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.runner	Running node 'retrieve_data_2' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Saving AsyncStringBuffer 'buffer_2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Persisting data for AsyncStringBuffer 'buffer_2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Loading cached data for IO 'process_data:data1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Loading cached data for IO 'process_data:data2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.runner	Running node 'process_data' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Saving AsyncStringBuffer 'buffer_3' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Persisting data for AsyncStringBuffer 'buffer_3' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Unpersisting data for IO 'process_data:data2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Unpersisting data for IO 'process_data:data1' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Unpersisting data for AsyncStringBuffer 'buffer_3' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Unpersisting data for AsyncStringBuffer 'buffer_2' in module 'example_async.async_ios_and_nodes'
DEBUG	ordeq.io	Unpersisting data for AsyncStringBuffer 'buffer_1' in module 'example_async.async_ios_and_nodes'
INFO	ordeq.io	Loading AsyncStringBuffer 'buffer_3' in module 'example_async.async_ios_and_nodes'

```