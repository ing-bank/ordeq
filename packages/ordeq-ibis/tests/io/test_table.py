import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisTable


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_loads_and_saves(df: pl.DataFrame, resource: str):
    """Test that IbisTable can save and load table data correctly."""
    table_name = "test_table"
    table_io = IbisTable(name=table_name, resource=resource)

    # Save the data
    table_io.save(ibis.memtable(df))

    # Load it back
    loaded = table_io.load()

    # Should be equal to original
    assert loaded.to_polars().equals(df)
