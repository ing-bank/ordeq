## Resource

```python
from example_async import async_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(async_nodes, fmt="mermaid"))
run(async_nodes)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "StringBuffer"}
	end

	example_async.async_nodes:write_buffer_1 --> example_async.async_nodes:buffer_1
	example_async.async_nodes:write_buffer_2 --> example_async.async_nodes:buffer_2

	example_async.async_nodes:write_buffer_1@{shape: rounded, label: "write_buffer_1"}
	example_async.async_nodes:write_buffer_2@{shape: rounded, label: "write_buffer_2"}
	example_async.async_nodes:buffer_1@{shape: rect, label: "buffer_1"}
	example_async.async_nodes:buffer_2@{shape: rect, label: "buffer_2"}

	class node_type,example_async.async_nodes:write_buffer_1,example_async.async_nodes:write_buffer_2 node
	class io_type_0,example_async.async_nodes:buffer_1,example_async.async_nodes:buffer_2 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

IOException: Failed to save 'buffer_1' in module 'example_async.async_nodes'.
string argument expected, got 'coroutine'
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _save_outputs
    output.save(data)
    ~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    _save_outputs(node.outputs, results)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/async/async_nodes.py", line LINO, in <module>
    run(async_nodes)
    ~~~^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Warnings

```text
RuntimeWarning: coroutine 'write_buffer_1' was never awaited
```

## Logging

```text
INFO	ordeq.runner	Running node 'write_buffer_1' in module 'example_async.async_nodes'
INFO	ordeq.io	Saving 'buffer_1' in module 'example_async.async_nodes'

```