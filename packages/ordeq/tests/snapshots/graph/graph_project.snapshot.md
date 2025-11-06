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
Node:example_project.inner.nodes:func --> io-1
Node:example_project.nodes:func --> io-2
Node:example_project.nodes_import:func_a --> io-3
Node:example_project.nodes_import:func_b --> io-4
Node:example_project.nodes_import_alias:func --> io-5
Node:example_project.nodes_import_reassign:func_a --> io-6
Node:example_project.nodes_import_reassign:func_b --> io-7
Node:example_project.nodes_with_inline_io:greet --> io-8
Node:example_project.nodes_with_view:farewell --> io-9
View:example_project.nodes_with_view:greet --> io-10
io-10 --> Node:example_project.nodes_with_view:farewell
NodeGraph
Node:example_project.inner.nodes:func
Node:example_project.nodes:func
Node:example_project.nodes_import:func_a
Node:example_project.nodes_import:func_b
Node:example_project.nodes_import_alias:func
Node:example_project.nodes_import_reassign:func_a
Node:example_project.nodes_import_reassign:func_b
Node:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_with_view:farewell
View:example_project.nodes_with_view:greet --> Node:example_project.nodes_with_view:farewell
Topological ordering
['example_project.nodes_with_view:greet',
 'example_project.nodes_with_view:farewell',
 'example_project.nodes_with_inline_io:greet',
 'example_project.nodes_import_reassign:func_b',
 'example_project.nodes_import_reassign:func_a',
 'example_project.nodes_import_alias:func',
 'example_project.nodes_import:func_b',
 'example_project.nodes_import:func_a',
 'example_project.nodes:func',
 'example_project.inner.nodes:func']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```