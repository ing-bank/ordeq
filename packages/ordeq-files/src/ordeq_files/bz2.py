import contextlib
from dataclasses import dataclass
from typing import Any, Literal, overload

from ordeq import IO
from ordeq.types import PathLike

with contextlib.suppress(ImportError):
    import bz2


@dataclass(frozen=True, kw_only=True)
class Bz2(IO[bytes | str]):
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
