# Captures loading and saving an IO with different load and save type.
# The save method has been overloaded to facilitate writing both bytes and str
# This example is highly artificial and should not be used as a reference when
# implementing IOs in practice.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import overload

from ordeq import Input, Output


@dataclass(kw_only=True, frozen=True, eq=False)
class Text(Input[str], Output[bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    @overload
    def save(self, data: str, encoding: str | None = None) -> None: ...

    @overload
    def save(self, data: bytes, encoding: None = None) -> None: ...

    def save(self, data: str | bytes, encoding: str | None = None) -> None:
        if isinstance(data, str):
            self.path.write_text(data, encoding)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example = Text(path=path)
    print("Should save to `example` with utf8 encoding:")
    example.save("some_string", encoding="utf8")
    print(path.read_text(encoding="utf8"))
    print("Should save to `example` in byte mode:")
    example.save(b"some_bytes")
    print(path.read_text(encoding="utf8"))
    print("Should fail because of unexpected argument:")
    example.save(b"some_bytes", x="x")
