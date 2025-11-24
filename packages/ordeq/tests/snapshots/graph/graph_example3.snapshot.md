## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_3
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_3)
nodes = [node for _, node in fqn_nodes]
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
View:View(func=example_3.func_defs:hello) --> io-0
View:View(func=example_3.func_defs:hello) --> io-1
NodeGraph
View:View(func=example_3.func_defs:hello)
View:View(func=example_3.func_defs:hello)
Topological ordering
(View(func=example_3.func_defs:hello), View(func=example_3.func_defs:hello))

```