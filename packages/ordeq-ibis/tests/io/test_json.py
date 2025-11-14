from pathlib import Path

import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisJSON


@pytest.mark.parametrize("resource", ["duckdb://", "polars://"])
def test_it_loads(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisJSON can load JSON files correctly."""
    path = tmp_path / "test_it_loads.json"
    df.write_ndjson(path)
    actual = IbisJSON(path=path, resource=resource).load()
    assert actual.to_polars().equals(df)


@pytest.mark.parametrize("resource", ["duckdb://"])
def test_it_saves(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisJSON can save JSON files correctly."""
    path = tmp_path / "test_it_saves.json"
    # Create backend and register table to avoid memtable issues
    io = IbisJSON(path=path, resource=resource)
    backend = io._backend
    table_name = "temp_table_for_json_test"
    backend.create_table(table_name, ibis.memtable(df), overwrite=True)
    table = backend.table(table_name)

    io.save(table)
    assert pl.read_json(path).equals(df)
