## Resource

```python
import example_anonymous
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_anonymous)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)

```

## Exception

```text
KeyError: 272593727
  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _add_io_data
    name=reverse_lookup[dataset_id],
         ~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    _add_io_data(input_dataset, reverse_lookup, io_data, store=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/to_mermaid.py", line LINO, in pipeline_to_mermaid
    node_modules, io_modules = _gather_graph(nodes, ios)
                               ~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/tests/resources/mermaid/viz_anonymous.py", line LINO, in <module>
    diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```