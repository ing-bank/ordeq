## Resource

```python

import example_imports.relative_import
from ordeq._scan import scan

print("Should raise an error:")
_ = scan(example_imports.relative_import)

```

## Output

```text
Should raise an error:
ValueError: Module 'example_imports.relative_import' aliases IO 'example_imports.relative_import:a' to 'b'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/scan/scan_relative_import.py", line LINO, in <module>
    _ = scan(example_imports.relative_import)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```