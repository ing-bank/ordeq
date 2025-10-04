from pathlib import Path

import polars as pl
from ordeq_polars import PolarsLazyCSV
from polars import LazyFrame


def test_it_loads_path(tmp_path: Path, lf: LazyFrame):
    path = tmp_path / "test_it_loads_path.csv"
    lf.sink_csv(path)
    assert PolarsLazyCSV(path=path).load().collect().equals(lf.collect())


def test_it_loads_str(tmp_path: Path, lf: LazyFrame):
    path = str(tmp_path / "test_it_loads_str.csv")
    lf.sink_csv(path)
    assert PolarsLazyCSV(path=path).load().collect().equals(lf.collect())


def test_it_saves_path(tmp_path: Path, lf: LazyFrame):
    path = tmp_path / "test_it_saves_path.csv"
    PolarsLazyCSV(path=path).save(lf)
    assert pl.read_csv(path).equals(lf.collect())


def test_it_saves_str(tmp_path: Path, lf: LazyFrame):
    path = str(tmp_path / "test_it_saves_str.csv")
    PolarsLazyCSV(path=path).save(lf)
    assert pl.read_csv(path).equals(lf.collect())
