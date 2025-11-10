## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_empty
from ordeq._graph import NamedNodeIOGraph, NodeGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_empty)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
pprint(named_node_io_graph)

node_graph = NodeGraph.from_graph(named_node_io_graph)
print("NodeGraph:")
pprint(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NamedNodeIOGraph:

NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {}), nodes={})
Topological ordering
()

```