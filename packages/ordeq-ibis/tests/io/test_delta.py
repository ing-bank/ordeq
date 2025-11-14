from pathlib import Path

import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisDelta


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_loads(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisDelta can load delta files correctly."""
    path = tmp_path / "test_it_loads.delta"
    ibis.connect(resource).to_delta(ibis.memtable(df), path)
    actual = IbisDelta(path=path, resource=resource).load()
    assert actual.to_polars().equals(df)


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_saves(tmp_path: Path, df: pl.DataFrame, resource: str):
    """Test that IbisDelta can save delta files correctly."""
    path = tmp_path / "test_it_saves.delta"
    IbisDelta(path=path, resource=resource).save(ibis.memtable(df))
    # Note: There's no direct polars read_delta, so we load back with Ibis
    loaded = ibis.connect(resource).read_delta(path)
    assert loaded.to_polars().equals(df)
