import json
from dataclasses import dataclass

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class JSON(IO[dict]):
    """IO representing a JSON.

    Example usage:

    ```pycon
    >>> from ordeq_files import JSON
    >>> from pathlib import Path
    >>> MyJSON = JSON(
    ...     path=Path("path/to.json")
    ... )

    ```

    """

    path: PathLike

    def load(self) -> dict:
        with self.path.open(mode="r") as fh:
            return json.load(fh)

    def save(self, data: dict) -> None:
        with self.path.open(mode="w") as fh:
            json.dump(data, fh)
