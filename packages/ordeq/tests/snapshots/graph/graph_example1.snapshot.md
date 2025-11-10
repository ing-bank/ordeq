## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_1
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_1)
node_io_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph:
<ordeq._graph.NodeIOGraph object at HASH1>
NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {Node(name=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]): {Node(name=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]): None}}), nodes={Node(name=example_1.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]): None, Node(name=example_1.pipeline:transform_input, inputs=[Input(idx=ID1)], outputs=[Output(idx=ID2)]): None, Node(name=example_1.pipeline:transform_mock_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)]): None, Node(name=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]): None, Node(name=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]): None})
Topological ordering:
(Node(name=example_1.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))]),
 Node(name=example_1.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()]))

```