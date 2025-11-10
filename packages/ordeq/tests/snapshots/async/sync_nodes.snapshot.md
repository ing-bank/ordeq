## Resource

```python
from example_async import sync_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(sync_nodes, fmt="mermaid"))
run(sync_nodes)

```

## Exception

```text
TypeError: 'Node' object is not iterable
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in _collect_views
    for node in nodes_:
                ^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    views = _collect_views(nodes)

  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    graph = NodeIOGraph.from_nodes(*nodes)

  File "/packages/ordeq-viz/src/ordeq_viz/to_mermaid.py", line LINO, in pipeline_to_mermaid
    node_modules, io_modules = _gather_graph(nodes, ios)
                               ~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    result = pipeline_to_mermaid(nodes, ios, **options)

  File "/packages/ordeq/tests/resources/async/sync_nodes.py", line LINO, in <module>
    print(viz(sync_nodes, fmt="mermaid"))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```