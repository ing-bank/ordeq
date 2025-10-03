from dataclasses import dataclass

import polars as pl
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PolarsEagerExcel(IO[pl.DataFrame]):
    """IO for loading and saving Excel using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsEagerExcel
    >>> from pathlib import Path
    >>> xlsx = PolarsEagerExcel(
    ...     path=Path("to.xlsx")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: PathLike

    def load(self, **load_options) -> pl.DataFrame:
        with self.path.open(mode="rb") as fh:
            return pl.read_excel(source=fh, **load_options)

    def save(self, df: pl.DataFrame, **save_options) -> None:
        with self.path.open(mode="wb") as fh:
            df.write_excel(workbook=fh, **save_options)
