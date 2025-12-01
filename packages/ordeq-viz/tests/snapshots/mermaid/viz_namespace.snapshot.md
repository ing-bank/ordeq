## Resource

```python
import example_namespace

from ordeq_viz import viz

diagram = viz(example_namespace, fmt="mermaid")
print(diagram)

```

## Output

```text
ValueError: Module 'example_namespace.namespace' aliases IO 'example_namespace.namespace:a' to 'B'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in _scan_fqns
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_process_nodes_and_ios.py", line LINO, in process_nodes_and_ios
    node_fqns, io_fqns = _scan_fqns(
                         ~~~~~~~~~~^
        *submodules_context, *submodules_to_process
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    nodes = process_nodes_and_ios(
        *vizzables, context=context_, node_filter=node_filter
    )

  File "/packages/ordeq-viz/tests/resources/mermaid/viz_namespace.py", line LINO, in <module>
    diagram = viz(example_namespace, fmt="mermaid")

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```