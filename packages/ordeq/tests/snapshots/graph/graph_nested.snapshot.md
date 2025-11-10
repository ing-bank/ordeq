## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_nested
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_nested)
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
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {}), nodes={View(name=example_nested.subpackage.subsubpackage.hello:world): None})
Topological ordering:
()

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_nested.subpackage.subsubpackage.hello:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```