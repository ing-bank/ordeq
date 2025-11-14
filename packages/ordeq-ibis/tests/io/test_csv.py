from pathlib import Path

import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisCSV


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_loads(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisCSV can load CSV files correctly."""
    path = tmp_path / "test_it_loads.csv"
    ibis.connect(resource).to_csv(ibis.memtable(df), path)
    actual = IbisCSV(path=path, resource=resource).load()
    assert actual.to_polars().equals(df)


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_saves(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisCSV can save CSV files correctly."""
    path = tmp_path / "test_it_saves.csv"
    IbisCSV(path=path, resource=resource).save(ibis.memtable(df))
    assert pl.read_csv(path).equals(df)
