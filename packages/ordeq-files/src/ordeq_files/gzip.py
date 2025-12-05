import contextlib
from dataclasses import dataclass
from typing import Any, Literal, overload

from ordeq import IO
from ordeq.types import PathLike

with contextlib.suppress(ImportError):
    import gzip


@dataclass(frozen=True, kw_only=True)
class Gzip(IO[bytes | str]):
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

    @overload
    def load(
        self,
        mode: Literal["r", "rb", "w", "wb", "x", "xb", "a", "ab"] = "rb",
        **load_options: Any,
    ) -> bytes: ...

    @overload
    def load(
        self, mode: Literal["rt", "wt", "xt", "at"] = "rt", **load_options: Any
    ) -> str: ...

    def load(self, mode: str = "rb", **load_options: Any) -> bytes | str:
        with gzip.open(self.path, mode=mode, **load_options) as f:
            return f.read()

    def save(
        self, data: str | bytes, mode: str = "wb", **save_options: Any
    ) -> None:
        with gzip.open(self.path, mode=mode, **save_options) as f:
            f.write(data)
