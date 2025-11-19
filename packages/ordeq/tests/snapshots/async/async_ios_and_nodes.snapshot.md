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
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "AsyncStringBuffer"}
	end

	example_async.async_ios_and_nodes:retrieve_data_1 --> IO0
	example_async.async_ios_and_nodes:retrieve_data_2 --> IO1
	IO0 --> example_async.async_ios_and_nodes:process_data
	IO1 --> example_async.async_ios_and_nodes:process_data
	example_async.async_ios_and_nodes:process_data --> IO2

	example_async.async_ios_and_nodes:retrieve_data_1@{shape: rounded, label: "retrieve_data_1"}
	example_async.async_ios_and_nodes:retrieve_data_2@{shape: rounded, label: "retrieve_data_2"}
	example_async.async_ios_and_nodes:process_data@{shape: rounded, label: "process_data"}
	IO0@{shape: rect, label: "buffer_1"}
	IO1@{shape: rect, label: "buffer_2"}
	IO2@{shape: rect, label: "buffer_3"}

	class L0,example_async.async_ios_and_nodes:retrieve_data_1,example_async.async_ios_and_nodes:retrieve_data_2,example_async.async_ios_and_nodes:process_data node
	class L00,IO0,IO1,IO2 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

Expect retrieve_data_2 node to complete before retrieve_data_1
Combined Data:


<coroutine object AsyncStringBuffer.load at HASH1>

```

## Warnings

```text
RuntimeWarning: coroutine 'AsyncStringBuffer.save' was never awaited
RuntimeWarning: coroutine 'retrieve_data_2' was never awaited
RuntimeWarning: coroutine 'AsyncStringBuffer.load' was never awaited
```

## Logging

```text
INFO	ordeq.runner	Running node "retrieve_data_1" in module "example_async.async_ios_and_nodes"
INFO	ordeq.io	Saving AsyncStringBuffer(_buffer=<_io.StringIO object at HASH2>, sleep_delay=1.0)
INFO	ordeq.runner	Running node "retrieve_data_2" in module "example_async.async_ios_and_nodes"
INFO	ordeq.io	Saving AsyncStringBuffer(_buffer=<_io.StringIO object at HASH3>, sleep_delay=2.0)
INFO	ordeq.runner	Running node "process_data" in module "example_async.async_ios_and_nodes"
INFO	ordeq.io	Saving AsyncStringBuffer(_buffer=<_io.StringIO object at HASH4>, sleep_delay=1.0)
INFO	ordeq.io	Loading AsyncStringBuffer(_buffer=<_io.StringIO object at HASH4>, sleep_delay=1.0)

```