import json
from dataclasses import dataclass
from typing import Any

from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class JSON(IO[dict[str, Any]]):
    """IO representing a JSON.

    Example usage:

    ```pycon
    >>> from ordeq_files import JSON
    >>> from pathlib import Path
    >>> my_json = JSON(
    ...     path=Path("path/to.json")
    ... )

    ```

    """

    path: PathLike

    def load(
        self, encoding: str = "utf-8", **load_options: Any
    ) -> dict[str, Any]:
        with self.path.open(mode="r", encoding=encoding) as fh:
            return json.load(fh, **load_options)

    def save(
        self,
        data: dict[str, Any],
        encoding: str = "utf-8",
        **save_options: Any,
    ) -> None:
        with self.path.open(mode="w", encoding=encoding) as fh:
            json.dump(data, fh, **save_options)
