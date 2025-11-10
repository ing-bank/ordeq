## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_anonymous)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph")
print(named_node_io_graph)

node_graph = NodeGraph.from_graph(named_node_io_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NamedNodeIOGraph
io-0 --> Node:example_anonymous.nodes:node_with_inline_io
Node:example_anonymous.nodes:node_with_inline_io --> io-1
NodeGraph

Topological ordering
[]

```