from pathlib import Path

import polars as pl
from ordeq_polars import PolarsEagerExcel


def test_it_loads_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads_path.xlsx"
    df.write_excel(path)
    assert PolarsEagerExcel(path=path).load().equals(df)


def test_it_loads_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_loads_str.xlsx")
    df.write_excel(path)
    assert PolarsEagerExcel(path=path).load().equals(df)


def test_it_saves_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves_path.xlsx"
    PolarsEagerExcel(path=path).save(df)
    assert pl.read_excel(path).equals(df)


def test_it_saves_str(tmp_path: Path, df: pl.DataFrame):
    path = str(tmp_path / "test_it_saves_str.xlsx")
    PolarsEagerExcel(path=path).save(df)
    assert pl.read_excel(path).equals(df)
