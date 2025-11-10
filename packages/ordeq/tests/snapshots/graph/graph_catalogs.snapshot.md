## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_catalogs
from ordeq._graph import NodeGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_catalogs)
node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {}), nodes={})
Topological ordering:
()

```