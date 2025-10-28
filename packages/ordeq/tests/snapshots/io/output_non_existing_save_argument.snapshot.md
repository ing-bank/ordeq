## Resource

```python
from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputsaveArg(Output):
    def save(self, data: str, hello: str = "...") -> None:
        pass


_ = ExampleOutputsaveArg().with_save_options(world="hello world")

```

## Exception

```text
TypeError: got an unexpected keyword argument 'world'
  File "/inspect.py", line LINO, in _bind
    raise TypeError(
        'got an unexpected keyword argument {arg!r}'.format(
            arg=next(iter(kwargs))))

  File "/inspect.py", line LINO, in bind_partial
    return self._bind(args, kwargs, partial=True)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in with_save_options
    inspect.signature(new_instance.save).bind_partial(**save_options)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/output_non_existing_save_argument.py", line LINO, in <module>
    _ = ExampleOutputsaveArg().with_save_options(world="hello world")

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```