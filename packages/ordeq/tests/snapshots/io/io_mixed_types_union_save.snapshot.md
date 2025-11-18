## Resource

```python
# Captures loading and saving an IO with different load and save type.
# The save type is a union of two data types.
# This example is highly artificial and should not be used as a reference when
# implementing IOs in practice.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile

from ordeq import Input, Output


@dataclass(kw_only=True, frozen=True)
class Text(Input[str], Output[bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    def save(self, data: str | bytes) -> None:
        if isinstance(data, str):
            self.path.write_text(data)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        # To clean the output
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example_input = Text(path=path)
    print(example_input.load())
    example_input.save("some_string")
    print(path.read_text(encoding="utf8"))
    example_input.save(b"some_bytes")
    print(path.read_text(encoding="utf8"))

```

## Output

```text
Text
some_string
some_bytes

```

## Logging

```text
INFO	ordeq.io	Loading Text
INFO	ordeq.io	Saving Text
INFO	ordeq.io	Saving Text

```