## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_nested
from ordeq._graph import NodeGraph, NodeIOGraph, ProjectGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_nested)
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
(View(name=example_nested.subpackage.subsubpackage.hello:world),
 IO(idx=ID1),
 Resource(IO(idx=ID1)))
NodeIOGraph:
View:example_nested.subpackage.subsubpackage.hello:world --> io-0
NodeGraph
View:example_nested.subpackage.subsubpackage.hello:world
Topological ordering
['example_nested.subpackage.subsubpackage.hello:world']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_nested.subpackage.subsubpackage.hello:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```