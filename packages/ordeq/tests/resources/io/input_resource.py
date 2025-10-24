from dataclasses import dataclass

from ordeq import Input
from pathlib import Path


@dataclass(kw_only=True, frozen=True)
class Inp(Input[str]):
    path: Path

    def load(self) -> str:
        return "Hello world"


f = Inp(path=Path('my.file'))
print(f.__resources__())


@dataclass(kw_only=True, frozen=True)
class File(Input[str]):
    path: Path

    def load(self) -> str:
        return "Hello world"

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]


f = File(path=Path('my.file'))
print(f.__resources__())
