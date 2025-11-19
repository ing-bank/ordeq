## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_function_reuse
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_function_reuse)
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
NodeGraph(edges={View(name=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [], View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]): [], View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]): [], View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]): [], View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): []})
Topological ordering
['example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.nodes:pi']

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