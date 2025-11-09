## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_project)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_graph(base_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
io-1 --> Node:example_project.nodes_import_reassign:func_b
io-1 --> Node:example_project.nodes_import_reassign:func_a
io-1 --> Node:example_project.nodes_import_alias:func
io-1 --> Node:example_project.nodes_import:func_a
io-1 --> Node:example_project.nodes_import:func_b
io-2 --> Node:example_project.nodes_import_reassign:func_b
io-2 --> Node:example_project.nodes_import_reassign:func_a
io-2 --> Node:example_project.nodes_import_alias:func
io-2 --> Node:example_project.nodes_import:func_a
io-2 --> Node:example_project.nodes_import:func_b
io-3 --> View:example_project.nodes_with_view:greet
io-4 --> Node:example_project.nodes:func
io-5 --> Node:example_project.inner.nodes:func
io-6 --> Node:example_project.nodes_with_inline_io:greet
io-7 --> Node:example_project.nodes_with_view:farewell
Node:example_project.nodes_import_reassign:func_b --> io-8
View:example_project.nodes_with_view:greet --> io-7
Node:example_project.nodes_import_reassign:func_a --> io-9
Node:example_project.nodes:func --> io-10
Node:example_project.nodes_import:func_a --> io-11
Node:example_project.inner.nodes:func --> io-12
Node:example_project.nodes_with_inline_io:greet --> io-13
Node:example_project.nodes_import_alias:func --> io-14
Node:example_project.nodes_with_view:farewell --> io-15
Node:example_project.nodes_import:func_b --> io-16
NodeGraph
Node:example_project.nodes_import_reassign:func_b
View:example_project.nodes_with_view:greet --> Node:example_project.nodes_with_view:farewell
Node:example_project.nodes_import_reassign:func_a
Node:example_project.nodes:func
Node:example_project.nodes_import:func_a
Node:example_project.inner.nodes:func
Node:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_import_alias:func
Node:example_project.nodes_with_view:farewell
Node:example_project.nodes_import:func_b
Topological ordering
['example_project.nodes_with_view:greet',
 'example_project.nodes_import:func_b',
 'example_project.nodes_import_alias:func',
 'example_project.nodes_with_inline_io:greet',
 'example_project.inner.nodes:func',
 'example_project.nodes_import:func_a',
 'example_project.nodes:func',
 'example_project.nodes_import_reassign:func_a',
 'example_project.nodes_with_view:farewell',
 'example_project.nodes_import_reassign:func_b']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```