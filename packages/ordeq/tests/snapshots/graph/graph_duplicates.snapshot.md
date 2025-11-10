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
pprint(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph:")
pprint(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph:
<ordeq._graph.NodeIOGraph object at HASH1>
NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {}),
          nodes={Node(name=example_duplicates.file1:foo, inputs=[Literal(3)], outputs=[IO(idx=ID1)]): None,
                 Node(name=example_duplicates.file2:foo, inputs=[Literal(3)], outputs=[IO(idx=ID2)]): None})
Topological ordering:
()

```