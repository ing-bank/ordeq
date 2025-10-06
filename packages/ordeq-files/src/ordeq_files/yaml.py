from dataclasses import dataclass

import yaml
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class YAML(IO[dict]):
    """IO representing a YAML.

    Example usage:

    ```pycon
    >>> from ordeq_files import YAML
    >>> from pathlib import Path
    >>> MyYAML = YAML(
    ...     path=Path("path/to.yaml")
    ... )

    ```

    """

    path: PathLike

    def load(self) -> dict:
        with self.path.open(mode="r") as fh:
            return yaml.safe_load(fh)

    def save(self, data: dict) -> None:
        with self.path.open(mode="w") as fh:
            yaml.safe_dump(data, fh)
