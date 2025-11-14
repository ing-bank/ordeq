from dataclasses import dataclass
from pathlib import Path
from typing import Any

import polars as pl
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PolarsLazyNdJSON(IO[pl.LazyFrame]):
    """IO to load lazily from newline-delimited JSON data using Polars.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_polars import PolarsLazyNdJSON
    >>> my_nd_json = PolarsLazyNdJSON(path=Path("path/to.ndjson"))

    ```

    """

    path: Path

    def load(self, **load_options: Any) -> pl.DataFrame:
        return pl.scan_ndjson(source=self.path, **load_options)
