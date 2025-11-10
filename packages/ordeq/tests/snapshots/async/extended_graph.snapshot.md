## Resource

```python
from example_async import extended_graph
from ordeq import run
from ordeq_viz import viz

print(viz(extended_graph, fmt="mermaid"))
run(extended_graph)

```

## Exception

```text
TypeError: NodeIOGraph.from_nodes() takes from 2 to 3 positional arguments but 8 were given
  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    graph = NodeIOGraph.from_nodes(*nodes)

  File "/packages/ordeq-viz/src/ordeq_viz/to_mermaid.py", line LINO, in pipeline_to_mermaid
    node_modules, io_modules = _gather_graph(nodes, ios)
                               ~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    result = pipeline_to_mermaid(nodes, ios, **options)

  File "/packages/ordeq/tests/resources/async/extended_graph.py", line LINO, in <module>
    print(viz(extended_graph, fmt="mermaid"))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```