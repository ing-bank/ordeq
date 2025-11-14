## Resource

```python
# Captures behaviour when setting None as resource
from pathlib import Path

from ordeq_files import CSV

csv = CSV(path=Path("my/path")) @ None

```

## Exception

```text
ValueError: Resource cannot be None.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in with_resource
    raise ValueError("Resource cannot be None.")

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __matmul__
    return self.with_resource(resource)
           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^

  File "/packages/ordeq/tests/resources/resources/none.py", line LINO, in <module>
    csv = CSV(path=Path("my/path")) @ None
          ~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```