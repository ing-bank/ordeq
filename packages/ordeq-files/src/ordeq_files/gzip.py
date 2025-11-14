import contextlib
from dataclasses import dataclass
from typing import Any

from ordeq import IO
from ordeq.types import PathLike

with contextlib.suppress(ImportError):
    import gzip


@dataclass(frozen=True, kw_only=True)
class Gzip(IO[bytes]):
    """IO representing a gzip-compressed file.

    Example usage:

    ```pycon
    >>> from ordeq_files import Gzip
    >>> from pathlib import Path
    >>> my_gzip = Gzip(
    ...     path=Path("path/to.gz")
    ... )

    ```

    """

    path: str | PathLike

    def load(self, mode="rb", **load_options: Any) -> bytes:
        with gzip.open(self.path, mode=mode, **load_options) as f:
            return f.read()

    def save(self, data: bytes, mode="wb", **save_options: Any) -> None:
        with gzip.open(self.path, mode=mode, **save_options) as f:
            f.write(data)
