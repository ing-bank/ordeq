## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_3
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_3)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
print(named_node_io_graph)

named_node_graph = NamedNodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)

```

## Output

```text
NamedNodeIOGraph:
View:example_3.func_defs:hello --> io-0
View:example_3.func_defs:hello --> io-1
NamedNodeGraph:

Topological ordering:
(View(name=example_3.func_defs:hello), View(name=example_3.func_defs:hello))

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```