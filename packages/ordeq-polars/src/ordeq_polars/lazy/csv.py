from dataclasses import dataclass
from pathlib import Path

import polars as pl
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PolarsLazyCSV(IO[pl.LazyFrame]):
    """IO for loading and saving CSV lazily using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsLazyCSV
    >>> from pathlib import Path
    >>> csv = PolarsLazyCSV(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: Path | str

    def load(self, **load_options) -> pl.LazyFrame:
        return pl.scan_csv(source=self.path, **load_options)

    def save(self, lf: pl.LazyFrame, **save_options) -> None:
        lf.sink_csv(path=self.path, **save_options)
