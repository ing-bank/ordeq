## Resource

```python
from dataclasses import dataclass

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input):
    def load(self) -> str:
        return "Hello world"


_ = ExampleInputLoadArg().with_load_options(hello="hello world")

```

## Exception

```text
TypeError: got an unexpected keyword argument 'hello'
  File "/inspect.py", line 3284, in _bind
    raise TypeError(
        'got an unexpected keyword argument {arg!r}'.format(
            arg=next(iter(kwargs))))

  File "/inspect.py", line 3302, in bind_partial
    return self._bind(args, kwargs, partial=True)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 158, in with_load_options
    inspect.signature(new_instance.load).bind_partial(**load_options)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/input_non_existing_load_argument.py", line 12, in <module>
    _ = ExampleInputLoadArg().with_load_options(hello="hello world")

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```