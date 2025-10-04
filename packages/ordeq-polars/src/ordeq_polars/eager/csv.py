from dataclasses import dataclass
from pathlib import Path

import polars as pl
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class PolarsEagerCSV(IO[pl.DataFrame]):
    """IO for loading and saving CSV using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsEagerCSV
    >>> from pathlib import Path
    >>> csv = PolarsEagerCSV(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: Path | str

    def load(self, **load_options) -> pl.DataFrame:
        return pl.read_csv(source=self.path, **load_options)  # type: ignore[arg-type]

    def save(self, df: pl.DataFrame, **save_options) -> None:
        df.write_csv(file=self.path, **save_options)
