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

    By default, lines are separated by newline characters
    during load.

    When saving, the newline character is appended to each line
    by default, this can be changed by providing a different `end` argument
    to the `save` method using `with_save_options`.

    Examples:

    ```pycon
    >>> from ordeq_files import TextLinesStream
    >>> from pathlib import Path
    >>> my_file = TextLinesStream(
    ...     path=Path("path/to.txt")
    ... )

    >>> my_file_no_endline = TextLinesStream(
    ...     path=Path("path/to.txt")
    ... ).with_save_options(end="")

    ```

    """

    path: PathLike

    def persist(self, _) -> None:
        """Don't persist since is a stream-based IO."""

    def __post_init__(self) -> None:
        logger.warning(
            "TextLinesStream is in pre-release, "
            "functionality may break in future releases "
            "without it being considered a breaking change."
        )

    def load(self, mode="r") -> Generator[str]:
        with self.path.open(mode=mode) as fh:
            yield from fh

    def save(self, data: Generator[str], mode="w", end="\n") -> None:
        with self.path.open(mode=mode) as fh:
            fh.writelines(f"{line}{end}" for line in data)
