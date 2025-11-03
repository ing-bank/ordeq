from collections.abc import Generator
from dataclasses import dataclass
from typing import TypeVar

from ordeq import IO
from ordeq.types import PathLike

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class FileStream(IO[Generator[T]]):
    """IO representing a file stream
    as a generator of lines.

    Useful for processing large files line-by-line.

    Examples:

    ```pycon
    >>> from ordeq_files import FileStream
    >>> from pathlib import Path
    >>> my_file = FileStream[str](
    ...     path=Path("path/to.txt")
    ... )

    ```

    """

    path: PathLike
    mode: str = "r+"

    def load(self) -> Generator[T, None, None]:
        with self.path.open(mode=self.mode) as fh:
            yield from fh.readlines()

    def save(self, data: Generator[T, None, None]) -> None:
        with self.path.open(mode=self.mode) as fh:
            fh.writelines(data)
