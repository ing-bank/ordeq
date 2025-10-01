from dataclasses import dataclass

import duckdb
from duckdb import DuckDBPyRelation
from ordeq import IO


@dataclass(frozen=True)
class DuckDBCSV(IO[DuckDBPyRelation]):
    """IO to load and save CSV files using DuckDB.

    Example in a node:

    ```python
    >>> from ordeq import node, run
    >>> from ordeq_duckdb import DuckDBCSV
    >>> connection = duckdb.connect(":memory:")
    >>> csv = DuckDBCSV(path="data.csv")
    >>> @node(outputs=csv)
    ... def create_data() -> duckdb.DuckDBPyRelation:
    ...     return connection.values([1, "a"])
    >>> result = run(create_data)
    >>> result[csv]
    ┌───────┬─────────┐
    │ col0  │  col1   │
    │ int32 │ varchar │
    ├───────┼─────────┤
    │     1 │ a       │
    └───────┴─────────┘
    <BLANKLINE>

    ```
    """

    path: str

    def load(self, **load_options) -> DuckDBPyRelation:
        """Load a CSV file into a DuckDBPyRelation.

        Args:
            load_options: Additional options to pass to duckdb.read_csv.

        Returns:
            A DuckDBPyRelation representing the loaded CSV data.
        """

        return duckdb.read_csv(self.path, **load_options)

    def save(self, relation: DuckDBPyRelation, **kwargs) -> None:
        """Save a DuckDBPyRelation to a CSV file.

        Args:
            relation: The DuckDBPyRelation to save.
            kwargs: Additional options to pass to relation.to_csv
        """

        relation.to_csv(self.path, **kwargs)
