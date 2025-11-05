## Resource

```python
# Captures the behaviour of an IO that doesn't cache loaded data.
# For some IOs, like streams and buffers, caching is counter-productive:
# repeated calls to `load()` should reload the data from scratch.
from dataclasses import dataclass

from ordeq import Input


@dataclass(kw_only=True)
class Counter(Input[int], cache=False):
    counter: int = 0

    def load(self) -> int:
        self.counter += 1
        return self.counter


counter = Counter()
print(counter.load())  # expect 1
print(counter.load())  # expect 2

```

## Exception

```text
TypeError: _InputMeta.__new__() got an unexpected keyword argument 'cache'
  File "/packages/ordeq/tests/resources/io/input_without_cache.py", line LINO, in <module>
    class Counter(Input[int], cache=False):
    ...<4 lines>...
            return self.counter

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```