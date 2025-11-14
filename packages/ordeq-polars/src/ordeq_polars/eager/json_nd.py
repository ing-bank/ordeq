from dataclasses import dataclass
from pathlib import Path
from typing import Any

import polars as pl
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PolarsEagerNdJSON(IO[pl.DataFrame]):
    """IO to load from and save to newline-delimited JSON data using Polars.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_polars import PolarsEagerNdJSON
    >>> my_nd_json = PolarsEagerNdJSON(path=Path("path/to.ndjson"))

    ```

    """

    path: str | Path

    def load(self, **load_options: Any) -> pl.DataFrame:
        return pl.read_ndjson(source=self.path, **load_options)

    def save(self, df: pl.DataFrame, **save_options: Any) -> None:
        df.write_ndjson(file=self.path, **save_options)
