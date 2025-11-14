from dataclasses import dataclass
from pathlib import Path
from typing import Any

import polars as pl
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PolarsEagerJSON(IO[pl.DataFrame]):
    """IO to load from and save to JSON data using Polars.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_polars import PolarsEagerJSON
    >>> my_json = PolarsEagerJSON(path=Path("path/to.json"))

    ```

    """

    path: str | Path

    def load(self, **load_options: Any) -> pl.DataFrame:
        return pl.read_json(source=self.path, **load_options)

    def save(self, df: pl.DataFrame, **save_options: Any) -> None:
        df.write_json(file=self.path, **save_options)
