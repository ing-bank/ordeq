## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_duplicates
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_duplicates)
base_graph = NodeIOGraph.from_nodes({node for _, _, node in nodes})
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
View:example_duplicates.duplicate_node_name:<lambda> --> io-1
Node:example_duplicates.file1:foo --> io-2
Node:example_duplicates.file2:foo --> io-3
io-4 --> Node:example_duplicates.file1:foo
io-5 --> Node:example_duplicates.file2:foo
NodeGraph
View:example_duplicates.duplicate_node_name:<lambda>
Node:example_duplicates.file1:foo
Node:example_duplicates.file2:foo
Topological ordering
['example_duplicates.file2:foo',
 'example_duplicates.file1:foo',
 'example_duplicates.duplicate_node_name:<lambda>']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_name:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_name:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```