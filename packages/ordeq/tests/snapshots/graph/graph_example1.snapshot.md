## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_1
from ordeq._graph import NodeGraph, NodeIOGraph, ProjectGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_1)
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

## Exception

```text
CycleError: ('nodes are in a cycle', [SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),)), Resource(SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))), SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))])
  File "/graphlib.py", line LINO, in prepare
    raise CycleError(f"nodes are in a cycle", cycle)

  File "/graphlib.py", line LINO, in static_order
    self.prepare()
    ~~~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in topological_ordering
    reversed(tuple(TopologicalSorter(self.edges).static_order()))
             ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/functools.py", line LINO, in __get__
    val = self.func(instance)

  File "/packages/ordeq/tests/resources/graph/graph_example1.py", line LINO, in <module>
    pprint(project_graph.topological_ordering)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Output

```text
Topological ordering:

```