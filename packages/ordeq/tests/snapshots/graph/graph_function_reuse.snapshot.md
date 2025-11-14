## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_function_reuse
from ordeq._graph import NodeGraph, NodeIOGraph, ProjectGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_function_reuse)
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
(Resource(StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 Resource(StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 Resource(StringBuffer(_buffer=<_io.StringIO object at HASH3>)),
 Resource(StringBuffer(_buffer=<_io.StringIO object at HASH4>)),
 StringBuffer(_buffer=<_io.StringIO object at HASH1>),
 StringBuffer(_buffer=<_io.StringIO object at HASH2>),
 StringBuffer(_buffer=<_io.StringIO object at HASH3>),
 StringBuffer(_buffer=<_io.StringIO object at HASH4>),
 View(name=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]),
 View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]),
 IO(idx=ID1),
 IO(idx=ID2),
 IO(idx=ID3),
 IO(idx=ID4),
 IO(idx=ID5),
 Resource(IO(idx=ID1)),
 Resource(IO(idx=ID2)),
 Resource(IO(idx=ID3)),
 Resource(IO(idx=ID4)),
 Resource(IO(idx=ID5)))
NodeIOGraph:
io-0 --> View:example_function_reuse.func_defs:print_input
io-0 --> View:example_function_reuse.nodes:pi
io-1 --> View:example_function_reuse.func_defs:print_input
io-2 --> View:example_function_reuse.func_defs:print_input
io-3 --> View:example_function_reuse.func_defs:print_input
View:example_function_reuse.nodes:pi --> io-4
View:example_function_reuse.func_defs:print_input --> io-5
View:example_function_reuse.func_defs:print_input --> io-6
View:example_function_reuse.func_defs:print_input --> io-7
View:example_function_reuse.func_defs:print_input --> io-8
NodeGraph
View:example_function_reuse.nodes:pi
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
Topological ordering
['example_function_reuse.nodes:pi',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.nodes:pi'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```