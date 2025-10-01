from dataclasses import dataclass
from pathlib import Path

import duckdb
from ordeq import Input


@dataclass(frozen=True)
class DuckDBConnection(Input[duckdb.DuckDBPyConnection]):
    """Input that loads a DuckDB connection."""

    database: str | Path = ":memory:"

    def load(self, **load_options) -> duckdb.DuckDBPyConnection:
        """Loads a DuckDB connection.

        Args:
            load_options: Additional options to pass to duckdb.connect.

        Returns:
            a DuckDBPyConnection.
        """

        return duckdb.connect(self.database, **load_options)
