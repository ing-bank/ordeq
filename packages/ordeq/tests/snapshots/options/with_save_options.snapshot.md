## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputSaveKwarg(Output):
    path: Path
    attribute: str

    def save(self, data: str, hello: str = "Guten tag") -> None:
        assert data == f"{self.path}@{self.attribute}: {hello} world!"


example_output = ExampleOutputSaveKwarg(path=Path("hello.txt"), attribute="L1")
# No kwarg:
example_output.save("hello.txt@L1: Guten tag world!")
# Alternative kwarg:
example_output.save("hello.txt@L1: Bonjour world!", hello="Bonjour")
print(type(example_output))

with_options = example_output.with_save_options(hello="Hello")
# No kwarg, with save options:
with_options.save("hello.txt@L1: Hello world!")
# Alternative kwarg, with save options:
with_options.save("hello.txt@L1: Buenos dias world!", hello="Buenos dias")
print(type(with_options))


@dataclass(kw_only=True, frozen=True)
class ExampleOutputSaveArg(Output):
    path: Path
    attribute: str

    def save(self, data: str, hello: str = "Hello") -> None:
        assert data == f"{self.path}@{self.attribute}: {hello} world!"


example_input_arg = ExampleOutputSaveArg(path=Path("hello.txt"), attribute="L1")
example_input_arg.save("hello.txt@L1: Hello world!", "Hello")
print(type(example_input_arg))

with_options_arg = example_input_arg.with_save_options(hello="Hello")
# This should raise a type error,
# but still run as we fill the missing arg on save:
with_options_arg.save("hello.txt@L1: Hello world!")
# Alternative arg, with save options:
with_options_arg.save("hello.txt@L1: Hi world!", hello="Hi")
print(type(with_options_arg))

example_input_arg.with_save_options(unknown_kwarg="Hello")  # should error

```

## Exception

```text
TypeError: got an unexpected keyword argument 'unknown_kwarg'
  File "/inspect.py", line 3284, in _bind
    raise TypeError(
        'got an unexpected keyword argument {arg!r}'.format(
            arg=next(iter(kwargs))))

  File "/inspect.py", line 3302, in bind_partial
    return self._bind(args, kwargs, partial=True)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 415, in with_save_options
    inspect.signature(new_instance.save).bind_partial(**save_options)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/options/with_save_options.py", line 52, in <module>
    example_input_arg.with_save_options(unknown_kwarg="Hello")  # should error
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
<class 'with_save_options.ExampleOutputSaveKwarg'>
<class 'with_save_options.ExampleOutputSaveKwarg'>
<class 'with_save_options.ExampleOutputSaveArg'>
<class 'with_save_options.ExampleOutputSaveArg'>

```

## Logging

```text
INFO	ordeq.io	Saving ExampleOutputSaveKwarg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveKwarg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveKwarg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveKwarg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveArg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveArg(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleOutputSaveArg(path=Path('hello.txt'), attribute='L1')

```