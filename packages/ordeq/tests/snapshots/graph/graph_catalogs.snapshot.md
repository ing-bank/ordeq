## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_catalogs
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_catalogs)
node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeGraph:

Topological ordering:
[]

```