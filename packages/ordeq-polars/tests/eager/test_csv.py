from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerCSV


def test_it_loads_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads_path.csv"
    df.write_csv(path)
    actual = PolarsEagerCSV(path=path).load()
    assert actual.equals(df)


def test_it_loads_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_loads_str.csv")
    df.write_csv(path)
    actual = PolarsEagerCSV(path=path).load()
    assert actual.equals(df)


def test_it_saves_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves_path.csv"
    PolarsEagerCSV(path=path).save(df)
    assert pl.read_csv(path).equals(df)


def test_it_saves_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_saves_str.csv")
    PolarsEagerCSV(path=path).save(df)
    assert pl.read_csv(path).equals(df)
