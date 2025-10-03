from pathlib import Path

import polars as pl
from ordeq_polars import PolarsLazyParquet


def test_it_loads_path(tmp_path: Path, lf: pl.LazyFrame):
    path = tmp_path / "test_it_loads_path.parquet"
    lf.sink_parquet(path)
    assert PolarsLazyParquet(path=path).load().collect().equals(lf.collect())


def test_it_loads_str(tmp_path: Path, lf: pl.LazyFrame):
    path = str(tmp_path / "test_it_loads_str.parquet")
    lf.sink_parquet(path)
    assert PolarsLazyParquet(path=path).load().collect().equals(lf.collect())


def test_it_saves_path(tmp_path: Path, lf: pl.LazyFrame):
    path = tmp_path / "test_it_saves_path.parquet"
    PolarsLazyParquet(path=path).save(lf)
    assert pl.read_parquet(path).equals(lf.collect())


def test_it_saves_str(tmp_path: Path, lf: pl.LazyFrame):
    path = str(tmp_path / "test_it_saves_str.parquet")
    PolarsLazyParquet(path=path).save(lf)
    assert pl.read_parquet(path).equals(lf.collect())
