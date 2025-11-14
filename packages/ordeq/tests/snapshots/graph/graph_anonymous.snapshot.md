## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_anonymous
from ordeq._graph import NodeGraph, ProjectGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_anonymous)
project_graph = ProjectGraph.from_nodes(nodes)
print("Topological ordering:")
pprint(project_graph.topological_ordering)

node_io_graph = NodeIOGraph.from_graph(project_graph)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
Topological ordering:
(Resource(IO(idx=ID1)),
 IO(idx=ID1),
 Node(name=example_anonymous.nodes:node_with_inline_io, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]),
 IO(idx=ID2),
 Resource(IO(idx=ID2)))
NodeIOGraph:
io-0 --> Node:example_anonymous.nodes:node_with_inline_io
Node:example_anonymous.nodes:node_with_inline_io --> io-1
NodeGraph
Node:example_anonymous.nodes:node_with_inline_io
Topological ordering
['example_anonymous.nodes:node_with_inline_io']

```