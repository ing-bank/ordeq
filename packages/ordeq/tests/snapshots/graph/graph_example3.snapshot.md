## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_3
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_3)
nodes = [node for _, _, node in fqn_nodes]
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
View:example_3.func_defs:hello --> io-0
View:example_3.func_defs:hello --> io-1
NodeGraph
View:example_3.func_defs:hello
View:example_3.func_defs:hello
Topological ordering
['example_3.func_defs:hello', 'example_3.func_defs:hello']

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```