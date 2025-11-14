from pathlib import Path

import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisXlsx


@pytest.mark.parametrize("resource", ["duckdb://"])
def test_it_loads(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisXlsx can load xlsx files correctly."""
    path = tmp_path / "test_it_loads.xlsx"
    # Create xlsx file using polars directly
    df.write_excel(path)
    actual = IbisXlsx(path=path, resource=resource).load()
    assert actual.to_polars().equals(df)


@pytest.mark.parametrize("resource", ["duckdb://"])
def test_it_saves(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisXlsx can save xlsx files correctly."""
    path = tmp_path / "test_it_saves.xlsx"
    IbisXlsx(path=path, resource=resource).save(ibis.memtable(df))
    assert pl.read_excel(path).equals(df)
