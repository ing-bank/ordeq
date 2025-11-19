## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_anonymous)
nodes = [node for _, _, node in fqn_nodes]
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
io-0 --> Node:example_anonymous.nodes:node_with_inline_io
Node:example_anonymous.nodes:node_with_inline_io --> io-1
NodeGraph
NodeGraph(edges={Node(name=example_anonymous.nodes:node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]): []})
Topological ordering
['example_anonymous.nodes:node_with_inline_io']

```