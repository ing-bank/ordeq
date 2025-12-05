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
io-0 --> View:example_anonymous.node_with_var_names:add
io-1 --> View:example_anonymous.node_with_var_names:add
io-2 --> Node:example_anonymous.nodes:node_with_inline_io
View:example_anonymous.node_with_var_names:add --> io-3
Node:example_anonymous.nodes:node_with_inline_io --> io-4
NodeGraph
Node:example_anonymous.nodes:node_with_inline_io --> Unit:example_anonymous.nodes:node_with_inline_io
View:example_anonymous.node_with_var_names:add --> Unit:example_anonymous.node_with_var_names:add
Topological ordering
(Unit(value=IO(id=ID1)),
 Unit(value=Input(id=ID2)),
 Unit(value=Input(id=ID3)),
 Node(module=example_anonymous.nodes, name=node_with_inline_io, inputs=[IO(id=ID1)], outputs=[IO(id=ID4)]),
 View(module=example_anonymous.node_with_var_names, name=add, inputs=[Input(id=ID3), Input(id=ID2)]),
 Unit(value=IO(id=ID4)),
 Unit(value=IO(id=ID5)))

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)

```