## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_2
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_2)
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
io-0 --> Node:example_2.nodes:transform_input_2
Node:example_2.nodes:transform_input_2 --> io-1
NodeGraph
Node:example_2.nodes:transform_input_2
Topological ordering
['example_2.nodes:transform_input_2']

```