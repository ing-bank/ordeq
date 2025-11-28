## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input[str]):
    path: Path
    attribute: str

    def load(self) -> int:
        return 3


example_input = ExampleInputLoadArg(path=Path("hello.txt"), attribute="L1")
print(example_input.load())

```

## Output

```text
3

```

## Logging

```text
INFO	ordeq.io	Loading ExampleInputLoadArg(path=Path('hello.txt'), attribute='L1')

```