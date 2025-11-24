## Resource

```python
import example_nested

from ordeq_viz import viz

diagram = viz(example_nested, fmt="mermaid", subgraphs=True)
print(diagram)

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

  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    node_graph = NodeGraph.from_nodes(nodes)

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    graph = _gather_graph(nodes_, ios)

  File "/packages/ordeq-viz/tests/resources/mermaid/viz_nested.py", line LINO, in <module>
    diagram = viz(example_nested, fmt="mermaid", subgraphs=True)

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
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```