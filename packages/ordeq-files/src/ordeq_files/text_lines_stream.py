from collections.abc import Generator
from dataclasses import dataclass

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class TextLinesStream(IO[Generator[str]]):
    """IO representing a file stream
    as a generator of lines.

    Useful for processing large files line-by-line.

    Examples:

    ```pycon
    >>> from ordeq_files import TextLineStream
    >>> from pathlib import Path
    >>> my_file = TextLineStream(
    ...     path=Path("path/to.txt")
    ... )

    ```

    """

    path: PathLike

    def load(self, mode="r") -> Generator[str, None, None]:
        with self.path.open(mode=mode) as fh:
            yield from fh

    def save(self, data: Generator[str, None, None], mode="w") -> None:
        with self.path.open(mode=mode) as fh:
            fh.writelines(data)
