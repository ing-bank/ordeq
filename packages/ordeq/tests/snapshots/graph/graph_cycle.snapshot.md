## Resource

```python
# Captures creation of a graph in case of node cycles
from example_resources import cycle
from ordeq._graph import BaseGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(cycle)
_ = BaseGraph.from_nodes(nodes)

```

## Exception

```text
ValueError: Nodes 'example_resources.cycle:generate_text' and 'example_resources.cycle:generate_raw' both output to resource Path('to.file'). Nodes cannot output to the same resource.
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    raise ValueError(
    ...<4 lines>...
    )

  File "/packages/ordeq/tests/resources/graph/graph_cycle.py", line LINO, in <module>
    _ = BaseGraph.from_nodes(nodes)

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