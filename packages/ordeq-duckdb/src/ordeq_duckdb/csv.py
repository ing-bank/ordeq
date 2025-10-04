from dataclasses import dataclass
from typing import Any

import duckdb
from ordeq import IO


@dataclass(frozen=True)
class DuckDBCSV(IO[duckdb.DuckDBPyRelation]):
    """IO to load and save CSV files using DuckDB.

    Example:

    ```pycon
    >>> from ordeq import node, run
    >>> from ordeq_duckdb import DuckDBCSV
    >>> csv = DuckDBCSV(path="data.csv")
    >>> csv.save(duckdb.values([1, "a"]))
    >>> data = csv.load()
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
        """Load a CSV file into a DuckDB relation.

        Args:
            **kwargs: Additional options to pass to duckdb.read_csv.

        Returns:
            The DuckDB relation representing the loaded CSV data.
        """

        return duckdb.read_csv(self.path, **kwargs)

    def save(self, relation: duckdb.DuckDBPyRelation, **kwargs: Any) -> None:
        """Save a DuckDB relation to a CSV file.

        Args:
            relation: The relation to save.
            **kwargs: Additional options to pass to `relation.to_csv`
        """

        relation.to_csv(self.path, **kwargs)
