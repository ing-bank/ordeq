from dataclasses import dataclass

import polars as pl
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PolarsEagerParquet(IO[pl.DataFrame]):
    """IO for loading and saving Parquet using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsEagerParquet
    >>> from pathlib import Path
    >>> csv = PolarsEagerParquet(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     n_rows=1_000
    ... )

    ```

    """

    path: PathLike

    def load(self, **load_options) -> pl.DataFrame:
        return pl.read_parquet(source=self.path, **load_options)  # type: ignore[arg-type]

    def save(self, df: pl.DataFrame, **save_options) -> None:
        with self.path.open(mode="wb") as fh:
            df.write_parquet(file=fh, **save_options)
