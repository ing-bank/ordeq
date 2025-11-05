## Resource

```python
# Captures the behaviour of an IO that doesn't cache saved data.
# For some IOs, like streams and buffers, caching is counter-productive:
# repeated calls to `load()` should reload the data from scratch.
from dataclasses import dataclass
from ordeq import IO


@dataclass(kw_only=True)
class Counter(IO[int], cache=False):
    counter: int = 0

    def save(self, _: int) -> None:
        self.counter += 1
        print(self.counter)


counter = Counter()
counter.save(123)  # expect 1
counter.save(123)  # expect 2

```

## Exception

```text
TypeError: _InputMeta.__new__() got an unexpected keyword argument 'cache'
  File "/packages/ordeq/tests/resources/io/output_without_cache.py", line LINO, in <module>
    class Counter(IO[int], cache=False):
    ...<4 lines>...
            print(self.counter)

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```