## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_function_reuse
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_function_reuse)
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
io-0 --> View:example_function_reuse.nodes:pi
io-0 --> View:example_function_reuse.func_defs:print_input
io-1 --> View:example_function_reuse.func_defs:print_input
io-2 --> View:example_function_reuse.func_defs:print_input
io-3 --> View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input --> io-4
View:example_function_reuse.func_defs:print_input --> io-5
View:example_function_reuse.func_defs:print_input --> io-6
View:example_function_reuse.func_defs:print_input --> io-7
View:example_function_reuse.nodes:pi --> io-8
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