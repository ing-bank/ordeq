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
io-0 --> Node:example_1.wrapped_io:hello
Node:example_1.wrapped_io:hello --> io-4
io-1 --> Node:example_1.nodes:world
io-2 --> Node:example_1.pipeline:transform_input
io-3 --> Node:example_1.pipeline:transform_mock_input
io-4 --> Node:example_1.wrapped_io:print_message
Node:example_1.nodes:world --> io-9
Node:example_1.pipeline:transform_input --> io-10
Node:example_1.pipeline:transform_mock_input --> io-11
Node:example_1.wrapped_io:print_message --> io-12
NodeGraph
Node:example_1.wrapped_io:hello --> Stub:example_1.wrapped_io:hello
Node:example_1.wrapped_io:print_message --> Stub:example_1.wrapped_io:print_message
Node:example_1.pipeline:transform_mock_input --> Stub:example_1.pipeline:transform_mock_input
Node:example_1.pipeline:transform_input --> Stub:example_1.pipeline:transform_input
Node:example_1.nodes:world --> Stub:example_1.nodes:world
Topological ordering
(Stub(value=NameGenerator(name='John')),
 Node(module=example_1.wrapped_io, name=hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Stub(value=SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))),
 Stub(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 Stub(value=Input(id=ID1)),
 Stub(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 Node(module=example_1.wrapped_io, name=print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]),
 Node(module=example_1.pipeline, name=transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]),
 Node(module=example_1.pipeline, name=transform_input, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)]),
 Node(module=example_1.nodes, name=world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]),
 Stub(value=NamePrinter()),
 Stub(value=StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 Stub(value=Output(id=ID2)),
 Stub(value=StringBuffer(_buffer=<_io.StringIO object at HASH4>)))

```