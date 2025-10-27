## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> str:
    return x


run(func)

```

## Exception

```text
ValueError: Node outputs invalid for return annotation: Node(name=node_with_returns_misses_outputs:func,...). Node has 0 output(s), but the return type annotation expects 1 value(s).
  File "/packages/ordeq/src/ordeq/_nodes.py", line 187, in _raise_for_invalid_outputs
    raise ValueError(
    ...<4 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 54, in validate
    _raise_for_invalid_outputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 45, in _run_node
    node.validate()
    ~~~~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 121, in _run_graph
    computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)

  File "/packages/ordeq/src/ordeq/_runner.py", line 191, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/nodes/node_with_returns_misses_outputs.py", line 10, in <module>
    run(func)
    ~~~^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```