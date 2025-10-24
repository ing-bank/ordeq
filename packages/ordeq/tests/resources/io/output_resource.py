from dataclasses import dataclass

from ordeq import Output
from pathlib import Path
from typing import Any


@dataclass(kw_only=True, frozen=True)
class Outp(Output[Any]):
    path: Path

    def save(self, data: Any) -> None:
        return


f = Outp(path=Path('my.file'))
print(f.__resources__())


@dataclass(kw_only=True, frozen=True)
class File(Output[Any]):
    path: Path

    def save(self, data: Any) -> None:
        return

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]


f = File(path=Path('my.file'))
print(f.__resources__())
