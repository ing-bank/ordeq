from dataclasses import dataclass
from typing import Literal

import polars as pl
from ordeq import Output

try:
    from pyiceberg.table import Table
except ImportError:

    class Table:  # type: ignore[no-redef]
        ...  # Placeholder if pyiceberg is not installed


@dataclass(frozen=True, kw_only=True)
class PolarsEagerIceberg(Output[pl.DataFrame]):
    """IO for saving Iceberg tables eagerly using Polars.

    Example:

    ```pycon
    >>> from ordeq_polars import PolarsEagerIceberg
    >>> iceberg = PolarsEagerIceberg(
    ...     path="file:/path/to/iceberg-table/metadata.json",
    ... )

    ```

    """

    path: str | Table

    def save(
        self, df: pl.DataFrame, mode: Literal["append", "overwrite"] = "append"
    ) -> None:
        """Write a DataFrame to an Iceberg table.

        Args:
            df: The DataFrame to write
            mode: The write mode ("append" or "overwrite")
        """

        df.write_iceberg(target=self.path, mode=mode)
