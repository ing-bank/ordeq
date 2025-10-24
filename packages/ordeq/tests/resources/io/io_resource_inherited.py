from dataclasses import dataclass

from ordeq import IO
from pathlib import Path
from typing import Any


@dataclass(kw_only=True, frozen=True)
class File(IO[str]):
    path: Path

    def load(self) -> str:
        return "data"

    def save(self, data: str) -> None:
        return

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]


@dataclass(frozen=True)
class CSV(File):
    fs: str

    def load(self) -> str:
        return "csv_data"

    def save(self, data: str) -> None:
        return

    def __resources__(self) -> list[str]:
        return [self.fs, self.path.__fspath__()]


f = CSV(path=Path('my.file'), fs='s3')
# Resources should be concatenated from base classes
print(f.__resources__())
