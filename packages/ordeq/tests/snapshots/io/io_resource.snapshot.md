## Resource

```python
from dataclasses import dataclass

from ordeq import IO
from pathlib import Path
from typing import Any


@dataclass(kw_only=True, frozen=True)
class Impl(IO[str]):
    path: Path

    def load(self) -> Any:
        return "data"

    def save(self, data: str) -> None:
        return


f = Impl(path=Path('my.file'))
print(f.__resources__())


@dataclass(kw_only=True, frozen=True)
class File(IO[str]):
    path: Path

    def load(self) -> str:
        return "data"

    def save(self, data: str) -> None:
        return

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]


f = File(path=Path('my.file'))
print(f.__resources__())

```

## Output

```text
[]
['my.file']

```

## Typing

```text
packages/ordeq/tests/resources/io/io_resource.py:37: error: Incompatible types in assignment (expression has type "File", variable has type "Impl")  [assignment]
Found 1 error in 1 file (checked 1 source file)

```