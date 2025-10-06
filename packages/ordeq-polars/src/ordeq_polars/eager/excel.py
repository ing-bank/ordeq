from dataclasses import dataclass
from pathlib import Path

import polars as pl
from ordeq.framework.io import IO


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

    path: Path | str

    def load(self, **load_options) -> pl.DataFrame:
        return pl.read_excel(source=self.path, **load_options)

    def save(self, df: pl.DataFrame, **save_options) -> None:
        df.write_excel(workbook=self.path, **save_options)
