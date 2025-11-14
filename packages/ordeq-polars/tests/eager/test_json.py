from pathlib import Path

import polars as pl
from ordeq_polars.eager import PolarsEagerJSON


def test_it_loads_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads_path.json"
    df.write_json(path)
    actual = PolarsEagerJSON(path=path).load()
    assert actual.equals(df)


def test_it_saves_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves_path.json"
    PolarsEagerJSON(path=path).save(df)
    assert pl.read_json(path).equals(df)
