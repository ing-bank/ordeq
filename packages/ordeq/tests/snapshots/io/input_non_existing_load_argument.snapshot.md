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

## Output

```text
TypeError: got an unexpected keyword argument 'hello'
  File "/inspect.py", line LINO, in _bind
    raise TypeError(
        'got an unexpected keyword argument {arg!r}'.format(
            arg=next(iter(kwargs))))

  File "/inspect.py", line LINO, in bind_partial
    return self._bind(args, kwargs, partial=True)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in with_load_options
    inspect.signature(new_instance.load).bind_partial(**load_options)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/input_non_existing_load_argument.py", line LINO, in <module>
    _ = ExampleInputLoadArg().with_load_options(hello="hello world")

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```