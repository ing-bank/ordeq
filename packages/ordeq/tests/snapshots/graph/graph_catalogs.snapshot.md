## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_catalogs
from ordeq._graph import NodeGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_catalogs)
node_graph = NodeGraph.from_nodes(*nodes)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)

```

## Exception

```text
TypeError: NodeGraph.from_nodes() missing 1 required positional argument: 'nodes'
  File "/packages/ordeq/tests/resources/graph/graph_catalogs.py", line LINO, in <module>
    node_graph = NodeGraph.from_nodes(*nodes)

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```