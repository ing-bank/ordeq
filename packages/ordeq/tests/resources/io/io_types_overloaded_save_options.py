# Captures loading and saving an IO with different load and save type.
# The save method has been overloaded to facilitate writing both bytes and
# text. This resource also captures the interaction of overloaded save
# methods with save options.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import overload

from ordeq import IO


@dataclass(kw_only=True, frozen=True)
class Text(IO[str, bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    @overload
    def save(self, data: str, encoding: str | None = None): ...

    @overload
    def save(self, data: bytes, encoding: None = None): ...

    def save(self, data: str | bytes, encoding: str | None = None) -> None:
        print("Saving with encoding", encoding)
        if isinstance(data, str):
            self.path.write_text(data, encoding)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        # To clean the output
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example = Text(path=path)
    example = example.with_save_options(encoding="utf8")
    example.save("some_bytes")
    example.save("some_bytes", encoding="koi8_t")
