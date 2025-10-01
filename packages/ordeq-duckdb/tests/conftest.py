import duckdb
import pytest
from duckdb import DuckDBPyConnection


@pytest.fixture
def connection() -> DuckDBPyConnection:
    return duckdb.connect(":memory:")
