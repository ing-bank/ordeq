from dataclasses import dataclass
from typing import Any, Literal

import polars as pl
from ordeq import IO
from pyiceberg.table import Table


@dataclass(frozen=True, kw_only=True)
class PolarsLazyIceberg(IO[pl.LazyFrame]):
    """IO for loading and saving Iceberg tables lazily using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars.lazy import PolarsLazyIceberg
    >>> iceberg = PolarsLazyIceberg(
    ...     path="file:/path/to/iceberg-table/metadata.json",
    ... )

    ```

    """

    path: str | Table

    def load(self, **load_options: Any) -> pl.LazyFrame:
        """Load an Iceberg table.

        Args:
            **load_options: Additional options passed to pl.read_iceberg.

        Returns:
            LazyFrame containing the Iceberg table data
        """
        return pl.scan_iceberg(source=self.path, **load_options)

    def save(
        self, lf: pl.LazyFrame, mode: Literal["append", "overwrite"] = "append"
    ) -> None:
        """Write a LazyFrame to an Iceberg table.

        Args:
            lf: The LazyFrame to write
            mode: The write mode ("append" or "overwrite")
        """

        lf.collect().write_iceberg(target=self.path, mode=mode)
