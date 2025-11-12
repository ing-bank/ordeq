## Resource

```python
# Captures the behaviour when resolving a module containing the same names
# for the same node.

from example_duplicates import duplicate_node_names
from ordeq._resolve import _resolve_module_to_nodes

_ = _resolve_module_to_nodes(duplicate_node_names)

```

## Exception

```text
ValueError: Module 'example_duplicates.duplicate_node_names' contains duplicate keys for the same node ('y' and 'x')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_nodes
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/resolve/resolve_duplicate_node_names.py", line LINO, in <module>
    _ = _resolve_module_to_nodes(duplicate_node_names)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```