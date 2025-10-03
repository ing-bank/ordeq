from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerParquet


def test_it_loads_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads_path.parquet"
    df.write_parquet(path)
    actual = PolarsEagerParquet(path=path).load()
    assert actual.equals(df)


def test_it_loads_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_loads_str.parquet")
    df.write_parquet(path)
    actual = PolarsEagerParquet(path=path).load()
    assert actual.equals(df)


def test_it_saves_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves_path.parquet"
    PolarsEagerParquet(path=path).save(df)
    assert pl.read_parquet(path).equals(df)


def test_it_saves_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_saves_str.parquet")
    PolarsEagerParquet(path=path).save(df)
    assert pl.read_parquet(path).equals(df)
