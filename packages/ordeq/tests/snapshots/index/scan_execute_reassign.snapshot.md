## Resource

```python
import example_imports.execute_reassign
from ordeq._index import index

print("Should raise an error:")
_ = index(example_imports.execute_reassign)

```

## Output

```text
Should raise an error:
ValueError: Module 'example_imports.execute_reassign' aliases IO 'example_imports.execute_reassign:a' to 'b'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_index.py", line LINO, in index
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/index/scan_execute_reassign.py", line LINO, in <module>
    _ = index(example_imports.execute_reassign)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```