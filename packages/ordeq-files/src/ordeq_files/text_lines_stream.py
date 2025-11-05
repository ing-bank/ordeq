import logging
from collections.abc import Generator
from dataclasses import dataclass

from ordeq import IO
from ordeq.types import PathLike

logger = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class TextLinesStream(IO[Generator[str]]):
    """IO representing a file stream
    as a generator of lines.

    Useful for processing large files line-by-line.

    Examples:

    ```pycon
    >>> from ordeq_files import TextLinesStream
    >>> from pathlib import Path
    >>> my_file = TextLinesStream(
    ...     path=Path("path/to.txt")
    ... )

    ```

    """

    path: PathLike

    def persist(self, _) -> None:
        """Don't persist since is a stream-based IO."""

    def __post_init__(self) -> None:
        logger.warning(
            "TextLinesStream is in pre-release, "
            "functionality may break in future releases "
        )

    def load(self, mode="r") -> Generator[str, None, None]:
        with self.path.open(mode=mode) as fh:
            yield from fh

    def save(self, data: Generator[str, None, None], mode="w") -> None:
        with self.path.open(mode=mode) as fh:
            fh.writelines(f"{line}\n" for line in data)
