import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisSQL


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_loads_with_query(df: pl.DataFrame, resource: str):
    """Test that IbisSQL can load data from SQL query."""
    # Create a connection and register the dataframe as a table
    table_name = "test_table"
    sql_io = IbisSQL(query=f"SELECT * FROM {table_name}", resource=resource)
    backend = sql_io._backend
    backend.create_table(table_name, ibis.memtable(df))

    # Use IbisSQL to query the table
    actual = sql_io.load()
    assert actual.to_polars().equals(df)
