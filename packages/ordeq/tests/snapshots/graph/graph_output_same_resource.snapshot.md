## Resource

```python
# Captures creation of a graph in case of node cycles
from example_resources import same_output
from ordeq._graph import BaseGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(same_output)
_ = BaseGraph.from_nodes(*nodes)

```

## Exception

```text
ModuleNotFoundError: No module named 'example_resources'
  File "/packages/ordeq/tests/resources/graph/graph_output_same_resource.py", line LINO, in <module>
    from example_resources import same_output

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/graph/graph_output_same_resource.py:2:6: error[unresolved-import] Cannot resolve imported module `example_resources`
packages/ordeq/tests/resources/graph/graph_output_same_resource.py:3:26: error[unresolved-import] Module `ordeq._graph` has no member `BaseGraph`
Found 2 diagnostics

```