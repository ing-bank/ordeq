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