## Resource

```python
# Captures the behaviour of an IO that doesn't cache loaded data.
# For some IOs, like streams and buffers, caching is counter-productive:
# repeated calls to `load()` should reload the data from scratch.
from dataclasses import dataclass

from ordeq import Input, node, run


@dataclass(kw_only=True)
class Counter(Input[int], cache=False):
    counter: int = 0

    def load(self) -> int:
        self.counter += 1
        return self.counter


counter = Counter()


@node(inputs=counter)
def func1(hello: str) -> None:
    print(hello)


@node(inputs=counter)
def func2(hello: str) -> None:
    print(hello)


run(func1, func2)
print(counter.counter)  # expect: 2

```

## Exception

```text
TypeError: _InputMeta.__new__() got an unexpected keyword argument 'cache'
  File "/packages/ordeq/tests/resources/runner/run_io_without_cache.py", line LINO, in <module>
    class Counter(Input[int], cache=False):
    ...<4 lines>...
            return self.counter

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```