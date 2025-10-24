## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import IO


@dataclass(kw_only=True, frozen=True)
class ExampleIO(IO[str]):
    path: Path
    attribute: str

    def load(self, hello: str = "Hello") -> str:
        return f"{self.path}@{self.attribute}: {hello} world!"

    def save(self, data: str, hello: str = "Hello") -> None:
        assert data == f"{self.path}@{self.attribute}: {hello} world!"


# Load:
example_input = ExampleIO(path=Path("hello.txt"), attribute="L1")
# No kwarg:
print(example_input.load())
# Alternative kwarg:
print(example_input.load(hello="Hello there"))

with_load_options = example_input.with_load_options(hello="Hey")
# No kwarg, with load options:
print(with_load_options.load())
# Alternative kwarg, with load options:
print(with_load_options.load(hello="Hi"))
print(type(with_load_options))

# Save:
example_output = ExampleIO(path=Path("world.txt"), attribute="L2")
# No kwarg:
example_output.save("world.txt@L2: Hello world!", hello="Hello")
# Alternative kwarg:
example_output.save("world.txt@L2: Guten tag world!", hello="Guten tag")

with_save_options = example_output.with_save_options(hello="Hey")
# No kwarg, with save options:
with_save_options.save("world.txt@L2: Hey world!")
# Alternative kwarg, with save options:
with_save_options.save("world.txt@L2: Hi world!", hello="Hi")
print(type(with_save_options))

```

## Output

```text
hello.txt@L1: Hello world!
hello.txt@L1: Hello there world!
hello.txt@L1: Hey world!
hello.txt@L1: Hi world!
<class 'io_complete.ExampleIO'>
<class 'io_complete.ExampleIO'>

```

## Logging

```text
INFO	ordeq.io	Loading ExampleIO(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Loading ExampleIO(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Loading ExampleIO(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Loading ExampleIO(path=Path('hello.txt'), attribute='L1')
INFO	ordeq.io	Saving ExampleIO(path=Path('world.txt'), attribute='L2')
INFO	ordeq.io	Saving ExampleIO(path=Path('world.txt'), attribute='L2')
INFO	ordeq.io	Saving ExampleIO(path=Path('world.txt'), attribute='L2')
INFO	ordeq.io	Saving ExampleIO(path=Path('world.txt'), attribute='L2')

```