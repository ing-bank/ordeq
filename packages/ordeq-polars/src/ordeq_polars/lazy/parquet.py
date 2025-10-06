from dataclasses import dataclass
from pathlib import Path

import polars as pl
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PolarsLazyParquet(IO[pl.LazyFrame]):
    """IO for loading and saving Parquet lazily using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsLazyParquet
    >>> from pathlib import Path
    >>> parquet = PolarsLazyParquet(
    ...     path=Path("to.parquet")
    ... ).with_load_options(
    ...     n_rows=1_000
    ... )

    ```

    """

    path: Path | str

    def load(self, **load_options) -> pl.LazyFrame:
        return pl.scan_parquet(source=self.path, **load_options)

    def save(self, lf: pl.LazyFrame, **save_options) -> None:
        lf.sink_parquet(self.path, **save_options)
