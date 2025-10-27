## Resource

```python
from ordeq import IO, Input, Output, node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = Input[str]()
I2 = Input[str]()
O1 = IO[str]()
O2 = Output[str]()


@node(inputs=[I1, I2], outputs=O1)
def f(i: str, j: str) -> str:
    return f"{i} {j}"


@node(inputs=O1, outputs=O2)
def g(a: str) -> str:
    return f(a, a)


print(run(f, g, verbose=True))  # raises NotImplementedError

```

## Exception

```text
IOException: Failed to load Input(idx=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line 241, in load_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 224, in load_wrapper
    return load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 194, in load_wrapper
    result = load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 170, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 170, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 79, in wrapper
    return composed(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line 55, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 138, in _run_graph
    computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)

  File "/packages/ordeq/src/ordeq/_runner.py", line 188, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/runner/incremental_placeholder.py", line 21, in <module>
    print(run(f, g, verbose=True))  # raises NotImplementedError
          ~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     incremental_placeholder:f -> [incremental_placeholder:g]
     incremental_placeholder:g -> []
  Nodes:
     Node(name=incremental_placeholder:f, inputs=[Input(idx=ID1), Input(idx=ID2)], outputs=[IO(idx=ID3)])
     Node(name=incremental_placeholder:g, inputs=[IO(idx=ID3)], outputs=[Output(idx=ID4)])

```

## Logging

```text
INFO	ordeq.io	Loading Input(idx=ID1)

```