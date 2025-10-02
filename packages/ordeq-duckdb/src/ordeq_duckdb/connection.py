from dataclasses import dataclass
from pathlib import Path
from typing import Any

import duckdb
from duckdb import DuckDBPyConnection
from ordeq import Input


@dataclass(frozen=True)
class DuckDBConnection(Input[DuckDBPyConnection]):
    """Input that loads a DuckDB connection."""

    database: str | Path = ":memory:"

    def load(self, **kwargs: Any) -> DuckDBPyConnection:
        """Loads a DuckDB connection.

        Args:
            **kwargs: Additional kwargs to pass to `duckdb.connect`.

        Returns:
            The DuckDB connection.
        """

        return duckdb.connect(self.database, **kwargs)
