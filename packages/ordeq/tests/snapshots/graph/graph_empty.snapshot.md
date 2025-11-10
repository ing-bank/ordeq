## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_empty
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_empty)
named_node_io_graph = NamedNodeIOGraph.from_nodes(*nodes)
print("NamedNodeIOGraph:")
print(named_node_io_graph)

named_node_graph = NamedNodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering")
pprint(named_node_graph.topological_ordering)

```

## Exception

```text
ImportError: cannot import name 'NamedNodeGraph' from 'ordeq._graph' (/packages/ordeq/src/ordeq/_graph.py)
  File "/packages/ordeq/tests/resources/graph/graph_empty.py", line LINO, in <module>
    from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/graph/graph_empty.py:5:26: error[unresolved-import] Module `ordeq._graph` has no member `NamedNodeGraph`
packages/ordeq/tests/resources/graph/graph_empty.py:5:42: error[unresolved-import] Module `ordeq._graph` has no member `NamedNodeIOGraph`
Found 2 diagnostics

```