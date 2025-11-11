## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_3
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_3)
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
View:example_3.func_defs:hello --> io-1
View:example_3.func_defs:hello --> io-2
NodeGraph
View:example_3.func_defs:hello
View:example_3.func_defs:hello
Topological ordering
['example_3.func_defs:hello', 'example_3.func_defs:hello']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```