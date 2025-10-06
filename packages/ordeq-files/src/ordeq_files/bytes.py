from dataclasses import dataclass

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class Bytes(IO[bytes]):
    """IO representing bytes.

    Example:

    ```pycon
    >>> from ordeq_files import Bytes
    >>> from pathlib import Path
    >>> my_png = Bytes(
    ...     path=Path("path/to.png")
    ... )

    ```

    """

    path: PathLike

    def load(self) -> bytes:
        with self.path.open(mode="rb") as fh:
            return fh.read()

    def save(self, data: bytes) -> None:
        with self.path.open(mode="wb") as fh:
            fh.write(data)
