## Resource

```python
from dataclasses import dataclass

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputNoLoad(Input): ...


_ = ExampleInputNoLoad()

```

## Exception

```text
TypeError: Can't instantiate abstract class ExampleInputNoLoad with abstract method load
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    raise TypeError(msg)

  File "/packages/ordeq/tests/resources/io/input_without_load.py", line LINO, in <module>
    class ExampleInputNoLoad(Input): ...

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```