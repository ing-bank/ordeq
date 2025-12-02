## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_anonymous)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
io-0 --> Node:example_anonymous.nodes:node_with_inline_io
io-1 --> View:example_anonymous.node_with_var_names:add
io-2 --> View:example_anonymous.node_with_var_names:add
Node:example_anonymous.nodes:node_with_inline_io --> io-3
View:example_anonymous.node_with_var_names:add --> io-4
NodeGraph
View:example_anonymous.node_with_var_names:add
Node:example_anonymous.nodes:node_with_inline_io
Topological ordering
(View(module=example_anonymous.node_with_var_names, name=add, inputs=[Input(id=ID1), Input(id=ID2)]),
 Node(module=example_anonymous.nodes, name=node_with_inline_io, inputs=[IO(id=ID3)], outputs=[IO(id=ID4)]))

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)

```