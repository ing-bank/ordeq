## Resource

```python
# Captures the behaviour when resolving a module containing the same
# object
from pprint import pprint

from example_duplicates import duplicate_io_objects
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(duplicate_io_objects)
pprint(ios)
assert hash(duplicate_io_objects.x) != hash(duplicate_io_objects.y)

```

## Exception

```text
ValueError: Module 'example_duplicates.duplicate_io_objects' contains duplicate keys for the same IO ('y' and 'x')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_ios
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/resolve/resolve_duplicate_io_objects.py", line LINO, in <module>
    ios = _resolve_module_to_ios(duplicate_io_objects)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```