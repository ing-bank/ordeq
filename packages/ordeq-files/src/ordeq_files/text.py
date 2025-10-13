from dataclasses import dataclass

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class Text(IO[str]):
    """IO representing a plain-text file.

    Examples:

    ```pycon
    >>> from ordeq_files import Text
    >>> from pathlib import Path
    >>> my_text = Text(
    ...     path=Path("path/to.txt")
    ... )

    ```

    """

    path: PathLike

    def load(self) -> str:
        with self.path.open(mode="r") as fh:
            return fh.read()

    def save(self, data: str) -> None:
        with self.path.open(mode="w") as fh:
            fh.write(data)
