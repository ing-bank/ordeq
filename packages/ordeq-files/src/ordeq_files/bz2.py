import contextlib
from dataclasses import dataclass
from typing import Any

from ordeq import IO
from ordeq.types import PathLike

with contextlib.suppress(ImportError):
    import bz2


@dataclass(frozen=True, kw_only=True)
class Bz2(IO[bytes]):
    """IO representing a bzip2-compressed file.

    Example usage:

    ```pycon
    >>> from ordeq_files import Bz2
    >>> from pathlib import Path
    >>> my_bz2 = Bz2(
    ...     path=Path("path/to.bz2")
    ... )

    ```

    """

    path: PathLike

    def load(self, mode="rb", **load_options: Any) -> bytes:
        with (
            self.path.open(mode) as fh,
            bz2.open(fh, mode=mode, **load_options) as f,
        ):
            return f.read()

    def save(self, data: bytes, mode="wb", **save_options: Any) -> None:
        with (
            self.path.open(mode) as fh,
            bz2.open(fh, mode=mode, **save_options) as f,
        ):
            f.write(data)
