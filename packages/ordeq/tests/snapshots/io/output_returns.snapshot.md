## Resource

```python
from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputNosave(Output):
    def save(self, data: str) -> str:
        return "hello"


_ = ExampleOutputNosave()

```

## Exception

```text
TypeError: Save method must have return type None.
  File "/packages/ordeq/src/ordeq/_io.py", line 380, in __new__
    raise TypeError("Save method must have return type None.")

  File "/packages/ordeq/tests/resources/io/output_returns.py", line 7, in <module>
    class ExampleOutputNosave(Output):
        def save(self, data: str) -> str:
            return "hello"

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```