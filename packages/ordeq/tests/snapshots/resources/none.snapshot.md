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

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```