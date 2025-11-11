from dataclasses import dataclass
from typing import Any

import polars as pl
from ordeq import IO

try:
    from pyiceberg.table import Table
except ImportError:

    class Table:  # type: ignore[no-redef]
        ...  # Placeholder if pyiceberg is not installed


@dataclass(frozen=True, kw_only=True)
class PolarsLazyIceberg(IO[pl.LazyFrame]):
    """IO for loading Iceberg tables lazily using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsLazyIceberg
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
