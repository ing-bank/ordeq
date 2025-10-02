import duckdb
import pytest


@pytest.fixture
def connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(":memory:")
