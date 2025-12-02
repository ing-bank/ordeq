## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_1
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_1)
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
io-0 --> Node:example_1.wrapped_io:print_message
io-1 --> Node:example_1.wrapped_io:hello
io-2 --> Node:example_1.pipeline:transform_mock_input
io-3 --> Node:example_1.pipeline:transform_input
io-4 --> Node:example_1.nodes:world
Node:example_1.wrapped_io:print_message --> io-5
Node:example_1.wrapped_io:hello --> io-6
Node:example_1.pipeline:transform_mock_input --> io-7
Node:example_1.pipeline:transform_input --> io-8
Node:example_1.nodes:world --> io-9
NodeGraph
Node:example_1.nodes:world
Node:example_1.pipeline:transform_input
Node:example_1.pipeline:transform_mock_input
Node:example_1.wrapped_io:hello
Node:example_1.wrapped_io:print_message
Topological ordering
(Node(module=example_1.nodes, name=world, inputs=[IO(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 Node(module=example_1.pipeline, name=transform_input, inputs=[IO(id=ID2)], outputs=[Output(id=ID3)]),
 Node(module=example_1.pipeline, name=transform_mock_input, inputs=[IO(id=ID4)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 Node(module=example_1.wrapped_io, name=hello, inputs=[IO(id=ID5)], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[IO(id=ID6)], outputs=[NamePrinter()]))

```