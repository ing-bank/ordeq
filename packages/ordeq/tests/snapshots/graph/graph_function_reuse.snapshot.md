## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_function_reuse
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_function_reuse)
nodes = [node for _, node in fqn_nodes]
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
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.func_defs:print_input
View:example_function_reuse.nodes:pi
Topological ordering
['example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.func_defs:print_input',
 'example_function_reuse.nodes:pi']

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.nodes:pi'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_function_reuse.func_defs:print_input'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```