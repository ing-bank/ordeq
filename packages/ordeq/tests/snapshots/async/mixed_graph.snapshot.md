## Resource

```python
from example_async import mixed_graph
from ordeq import run
from ordeq_viz import viz

print(viz(mixed_graph, fmt="mermaid"))
run(mixed_graph)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_async.mixed_graph:process_buffer
	example_async.mixed_graph:process_buffer --> IO1
	example_async.mixed_graph:write_buffer_1 --> IO2
	example_async.mixed_graph:write_buffer_2 --> IO0

	example_async.mixed_graph:process_buffer@{shape: rounded, label: "process_buffer"}
	example_async.mixed_graph:write_buffer_1@{shape: rounded, label: "write_buffer_1"}
	example_async.mixed_graph:write_buffer_2@{shape: rounded, label: "write_buffer_2"}
	IO0@{shape: rect, label: "buffer_2"}
	IO1@{shape: rect, label: "processed_buffer"}
	IO2@{shape: rect, label: "buffer_1"}

	class L0,example_async.mixed_graph:process_buffer,example_async.mixed_graph:write_buffer_1,example_async.mixed_graph:write_buffer_2 node
	class L00,IO0,IO1,IO2 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

IOException: Failed to save StringBuffer(_buffer=<_io.StringIO object at HASH1>).
string argument expected, got 'coroutine'
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **kwargs)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    composed(data, *args, **kwargs)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    output.save(data)
    ~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/async/mixed_graph.py", line LINO, in <module>
    run(mixed_graph)
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
RuntimeWarning: coroutine 'write_buffer_2' was never awaited
```

## Logging

```text
INFO	ordeq.runner	Running node "write_buffer_2" in module "example_async.mixed_graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```