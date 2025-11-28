## Resource

```python
# Captures loading and saving an IO with different load and save type.
# The save method has been overloaded to facilitate writing both bytes and str
# This example is highly artificial and should not be used as a reference when
# implementing IOs in practice.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import overload

from ordeq import Input, Output


@dataclass(kw_only=True, frozen=True)
class Text(Input[str], Output[bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    @overload
    def save(self, data: str): ...

    @overload
    def save(self, data: bytes): ...

    def save(self, data: str | bytes) -> None:
        if isinstance(data, str):
            self.path.write_text(data, "utf8")
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example = Text(path=path)
    print("Should save to `example` with utf8 encoding:")
    example.save("some_string")
    print(path.read_text(encoding="utf8"))
    print("Should save to `example` in byte mode:")
    example.save(b"some_bytes")
    print(path.read_text(encoding="utf8"))
    print("Should fail because of unexpected argument:")
    example.save(b"some_bytes", x="x")

```

## Output

```text
Should save to `example` with utf8 encoding:
some_string
Should save to `example` in byte mode:
some_bytes
Should fail because of unexpected argument:
IOException: Failed to save Text.
Text.save() got an unexpected keyword argument 'x'
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save.py", line LINO, in <module>
    example.save(b"some_bytes", x="x")
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Saving Text
INFO	ordeq.io	Saving Text
INFO	ordeq.io	Saving Text

```