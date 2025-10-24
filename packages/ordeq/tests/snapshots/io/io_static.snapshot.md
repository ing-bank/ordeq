## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import IO


class ExampleStaticIO(IO[str]):
    @staticmethod
    def load() -> str:
        return "loaded"

    @staticmethod
    def save(data: str) -> None:
        print(data)


# This currently raises an exception because the first argument of `save` needs
# to be `self`.
example_io = ExampleStaticIO()
print(example_io.load())
print(example_io.save("saved"))

```

## Exception

```text
TypeError: Save method requires a data parameter.
```