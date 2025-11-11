## Resource

```python
from example_async import extended_graph
from ordeq import run
from ordeq_viz import viz

print(viz(extended_graph, fmt="mermaid"))
run(extended_graph)

```

## Exception

```text
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

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _save_outputs
    output_dataset.save(data)
    ~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    _save_outputs(node, values, save=save)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks, save=save_node)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "StringBuffer"}
	end

	example_async.extended_graph:write_A --> IO0
	example_async.extended_graph:write_B --> IO1
	IO0 --> example_async.extended_graph:write_C
	IO1 --> example_async.extended_graph:write_C
	example_async.extended_graph:write_C --> IO2
	example_async.extended_graph:write_D --> IO3
	example_async.extended_graph:write_E --> IO4
	IO3 --> example_async.extended_graph:write_F
	IO4 --> example_async.extended_graph:write_F
	example_async.extended_graph:write_F --> IO5
	IO2 --> example_async.extended_graph:write_G
	IO5 --> example_async.extended_graph:write_G
	example_async.extended_graph:write_G --> IO6

	example_async.extended_graph:write_A@{shape: rounded, label: "write_A"}
	example_async.extended_graph:write_B@{shape: rounded, label: "write_B"}
	example_async.extended_graph:write_C@{shape: rounded, label: "write_C"}
	example_async.extended_graph:write_D@{shape: rounded, label: "write_D"}
	example_async.extended_graph:write_E@{shape: rounded, label: "write_E"}
	example_async.extended_graph:write_F@{shape: rounded, label: "write_F"}
	example_async.extended_graph:write_G@{shape: rounded, label: "write_G"}
	IO0@{shape: rect, label: "A"}
	IO1@{shape: rect, label: "B"}
	IO2@{shape: rect, label: "C"}
	IO3@{shape: rect, label: "D"}
	IO4@{shape: rect, label: "E"}
	IO5@{shape: rect, label: "F"}
	IO6@{shape: rect, label: "G"}

	class L0,example_async.extended_graph:write_A,example_async.extended_graph:write_B,example_async.extended_graph:write_C,example_async.extended_graph:write_D,example_async.extended_graph:write_E,example_async.extended_graph:write_F,example_async.extended_graph:write_G node
	class L00,IO0,IO1,IO2,IO3,IO4,IO5,IO6 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Warnings

```text
RuntimeWarning: coroutine 'write_E' was never awaited
```

## Logging

```text
INFO	ordeq.runner	Running node "write_E" in module "example_async.extended_graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```