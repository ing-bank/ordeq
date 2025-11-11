## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_anonymous)
base_graph = NodeIOGraph.from_nodes({node for _, _, node in nodes})
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
Node:example_anonymous.nodes:node_with_inline_io --> io-1
io-2 --> Node:example_anonymous.nodes:node_with_inline_io
NodeGraph
Node:example_anonymous.nodes:node_with_inline_io
Topological ordering
['example_anonymous.nodes:node_with_inline_io']

```