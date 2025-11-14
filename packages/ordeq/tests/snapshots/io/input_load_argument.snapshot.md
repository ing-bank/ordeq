## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input):
    path: Path
    attribute: str

    def load(self, hello: str = "...") -> str:
        """My docstring"""
        return f"{self.path}@{self.attribute}: {hello} world!"


example_input = ExampleInputLoadArg(path=Path("hello.txt"), attribute="L1")
print(example_input.load("Hello"))

```

## Output

```text
hello.txt@L1: Hello world!

```

## Logging

```text
INFO	ordeq.io	Loading ExampleInputLoadArg(path=Path('hello.txt'), attribute='L1')

```