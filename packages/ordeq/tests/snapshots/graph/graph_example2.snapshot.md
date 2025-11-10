## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_2
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_2)
named_node_io_graph = NamedNodeIOGraph.from_nodes(*nodes)
print("NamedNodeIOGraph:")
print(named_node_io_graph)

named_node_graph = NamedNodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)

```

## Output

```text
NamedNodeIOGraph:
io-0 --> Node:example_2.nodes:transform_input_2
Node:example_2.nodes:transform_input_2 --> io-1
NamedNodeGraph:

Topological ordering:
(Node(name=example_2.nodes:transform_input_2, inputs=[Input(idx=ID1)], outputs=[Output(idx=ID2)]),)

```