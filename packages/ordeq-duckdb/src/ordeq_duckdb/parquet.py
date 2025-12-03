from dataclasses import dataclass
from typing import Any

import duckdb
from ordeq import IO


@dataclass(frozen=True)
class DuckDBParquet(IO[duckdb.DuckDBPyRelation]):
    """IO to load and save Parquet files using DuckDB.

    Example:

    ```pycon
    >>> from ordeq import node, run
    >>> from ordeq_duckdb import DuckDBCSV
    >>> parquet = DuckDBParquet(path="data.csv")
    >>> parquet.save(duckdb.values([1, "a"]))
    >>> data = parquet.load()
    >>> data.describe()
    ┌─────────┬────────┬─────────┐
    │  aggr   │  col0  │  col1   │
    │ varchar │ double │ varchar │
    ├─────────┼────────┼─────────┤
    │ count   │    1.0 │ 1       │
    │ mean    │    1.0 │ NULL    │
    │ stddev  │   NULL │ NULL    │
    │ min     │    1.0 │ a       │
    │ max     │    1.0 │ a       │
    │ median  │    1.0 │ NULL    │
    └─────────┴────────┴─────────┘
    <BLANKLINE>

    ```

    """

    path: str

    def load(self, **kwargs: Any) -> duckdb.DuckDBPyRelation:
        """Load a Parquet file into a DuckDB relation.

        Args:
            **kwargs: Additional options to pass to duckdb.read_parquet.

        Returns:
            The DuckDB relation representing the loaded Parquet data.
        """

        return duckdb.read_parquet(self.path, **kwargs)

    def save(self, relation: duckdb.DuckDBPyRelation, **kwargs: Any) -> None:
        """Save a DuckDB relation to a Parquet file.

        Args:
            relation: The relation to save.
            **kwargs: Additional options to pass to `relation.to_parquet`
        """

        relation.to_parquet(self.path, **kwargs)
