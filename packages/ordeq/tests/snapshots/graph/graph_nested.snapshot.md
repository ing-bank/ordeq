## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_nested
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_nested)
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
Relativistic mass
ValueError: Nodes 'example_nested.subpackage.subsubpackage.hello_relative:world_relative' and 'example_nested.subpackage.subsubpackage.hello_relative:world_relative' both output to Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)). Nodes cannot output to the same resource.
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    raise ValueError(msg)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeResourceGraph.from_nodes(nodes))
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeGraph.from_nodes(nodes))
                          ~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq/tests/resources/graph/graph_nested.py", line LINO, in <module>
    base_graph = NodeIOGraph.from_nodes(nodes)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.runner	Running node 'world_relative' in module 'example_nested.subpackage.subsubpackage.hello_relative'
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```