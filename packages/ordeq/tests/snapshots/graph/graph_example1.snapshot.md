## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_1
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_1)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
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
io-0 --> Node:example_1.nodes:world
io-2 --> Node:example_1.pipeline:transform_input
io-4 --> Node:example_1.pipeline:transform_mock_input
io-6 --> Node:example_1.wrapped_io:hello
io-7 --> Node:example_1.wrapped_io:print_message
Node:example_1.nodes:world --> io-1
Node:example_1.pipeline:transform_input --> io-3
Node:example_1.pipeline:transform_mock_input --> io-5
Node:example_1.wrapped_io:hello --> io-7
Node:example_1.wrapped_io:print_message --> io-8
NamedNodeGraph:
Node:example_1.wrapped_io:hello --> Node:example_1.wrapped_io:print_message
Topological ordering:
(Node(name=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(name=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]),
 Node(name=example_1.pipeline:transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 Node(name=example_1.pipeline:transform_input, inputs=[Input(idx=ID1)], outputs=[Output(idx=ID2)]),
 Node(name=example_1.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]))

```