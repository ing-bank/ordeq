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
ImportError: cannot import name 'BaseGraph' from 'ordeq._graph' (/packages/ordeq/src/ordeq/_graph.py)
  File "/packages/ordeq/tests/resources/graph/graph_output_same_resource.py", line LINO, in <module>
    from ordeq._graph import BaseGraph

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.
WARNING	ordeq.io	The syntax 'IO @ resource' is in preview mode and may change without notice in future releases.

```

## Typing

```text
packages/ordeq/tests/resources/graph/graph_output_same_resource.py:3:26: error[unresolved-import] Module `ordeq._graph` has no member `BaseGraph`
Found 1 diagnostic

```