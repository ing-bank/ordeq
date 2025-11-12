## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_duplicates
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_duplicates)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_graph(base_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Exception

```text
ValueError: Module 'example_duplicates.duplicate_node_objects' contains duplicate keys for the same node ('y' and 'x')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_nodes
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes
    nodes.update(_resolve_module_to_nodes(module).values())
                 ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/graph/graph_duplicates.py", line LINO, in <module>
    nodes = _resolve_runnables_to_nodes(example_duplicates)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_names:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_objects:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```