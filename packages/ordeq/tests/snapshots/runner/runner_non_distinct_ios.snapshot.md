## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


@node(outputs=x)
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)

```

## Exception

```text
ValueError: IO StringBuffer(_buffer=<_io.StringIO object at HASH1>) cannot be outputted by more than one node
  File "/packages/ordeq/src/ordeq/_graph.py", line 58, in _build_graph
    raise ValueError(msg)

  File "/packages/ordeq/src/ordeq/_graph.py", line 115, in from_nodes
    return cls(_build_graph(nodes | views))
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 172, in run
    graph = NodeGraph.from_nodes(nodes)

  File "/packages/ordeq/tests/resources/runner/runner_non_distinct_ios.py", line 17, in <module>
    run(func1, func2, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```