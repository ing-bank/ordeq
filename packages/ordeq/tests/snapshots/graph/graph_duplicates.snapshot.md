## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_duplicates
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_duplicates)
node_io_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph:
io-1 --> Node:example_duplicates.file1:foo
io-2 --> Node:example_duplicates.file2:foo
Node:example_duplicates.file1:foo --> io-3
Node:example_duplicates.file2:foo --> io-4
NodeGraph:
Node:example_duplicates.file2:foo
Node:example_duplicates.file1:foo
Topological ordering:
['example_duplicates.file1:foo', 'example_duplicates.file2:foo']

```