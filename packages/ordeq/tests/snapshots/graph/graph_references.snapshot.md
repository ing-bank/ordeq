## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_references
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_references)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_graph(base_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
<ordeq._graph.NodeIOGraph object at HASH1>
NodeGraph

Topological ordering
[]

```