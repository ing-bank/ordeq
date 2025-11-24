## Resource

```python
import example_imports.execute_reassign
from ordeq._scan import _scan_fqns

print("Should raise an error:")
_ = _scan_fqns(example_imports.execute_reassign)

```

## Output

```text
Should raise an error:
ValueError: Module 'example_imports.execute_reassign' aliases IO 'example_imports.execute_reassign:a' to 'b'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in _scan_fqns
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/scan/scan_execute_reassign.py", line LINO, in <module>
    _ = _scan_fqns(example_imports.execute_reassign)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```