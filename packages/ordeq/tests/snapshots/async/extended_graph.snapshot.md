## Resource

```python
from example_async import extended_graph
from ordeq import run
from ordeq_viz import viz

print(viz(extended_graph, fmt="mermaid"))
run(extended_graph)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "StringBuffer"}
	end

	example_async.extended_graph:write_A --> example_async.extended_graph:A
	example_async.extended_graph:write_B --> example_async.extended_graph:B
	example_async.extended_graph:write_D --> example_async.extended_graph:D
	example_async.extended_graph:write_E --> example_async.extended_graph:E
	example_async.extended_graph:A --> example_async.extended_graph:write_C
	example_async.extended_graph:B --> example_async.extended_graph:write_C
	example_async.extended_graph:write_C --> example_async.extended_graph:C
	example_async.extended_graph:D --> example_async.extended_graph:write_F
	example_async.extended_graph:E --> example_async.extended_graph:write_F
	example_async.extended_graph:write_F --> example_async.extended_graph:F
	example_async.extended_graph:C --> example_async.extended_graph:write_G
	example_async.extended_graph:F --> example_async.extended_graph:write_G
	example_async.extended_graph:write_G --> example_async.extended_graph:G

	example_async.extended_graph:write_A@{shape: rounded, label: "write_A"}
	example_async.extended_graph:write_B@{shape: rounded, label: "write_B"}
	example_async.extended_graph:write_D@{shape: rounded, label: "write_D"}
	example_async.extended_graph:write_E@{shape: rounded, label: "write_E"}
	example_async.extended_graph:write_C@{shape: rounded, label: "write_C"}
	example_async.extended_graph:write_F@{shape: rounded, label: "write_F"}
	example_async.extended_graph:write_G@{shape: rounded, label: "write_G"}
	example_async.extended_graph:A@{shape: rect, label: "A"}
	example_async.extended_graph:B@{shape: rect, label: "B"}
	example_async.extended_graph:C@{shape: rect, label: "C"}
	example_async.extended_graph:D@{shape: rect, label: "D"}
	example_async.extended_graph:E@{shape: rect, label: "E"}
	example_async.extended_graph:F@{shape: rect, label: "F"}
	example_async.extended_graph:G@{shape: rect, label: "G"}

	class node_type,example_async.extended_graph:write_A,example_async.extended_graph:write_B,example_async.extended_graph:write_D,example_async.extended_graph:write_E,example_async.extended_graph:write_C,example_async.extended_graph:write_F,example_async.extended_graph:write_G node
	class io_type_0,example_async.extended_graph:A,example_async.extended_graph:B,example_async.extended_graph:C,example_async.extended_graph:D,example_async.extended_graph:E,example_async.extended_graph:F,example_async.extended_graph:G io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

IOException: Failed to save StringBuffer 'A' in module 'example_async.extended_graph'.
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

  File "/packages/ordeq/tests/resources/async/extended_graph.py", line LINO, in <module>
    run(extended_graph)
    ~~~^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Warnings

```text
RuntimeWarning: coroutine 'write_A' was never awaited
```

## Logging

```text
INFO	ordeq.runner	Running node 'write_A' in module 'example_async.extended_graph'
INFO	ordeq.io	Saving StringBuffer 'A' in module 'example_async.extended_graph'

```