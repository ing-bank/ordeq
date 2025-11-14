from pathlib import Path

import polars as pl
from ordeq_polars.eager import PolarsEagerNdJSON


def test_it_loads_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_loads_path.ndjson"
    df.write_ndjson(path)
    actual = PolarsEagerNdJSON(path=path).load()
    assert actual.equals(df)


def test_it_saves_path(tmp_path: Path, df: pl.DataFrame):
    path = tmp_path / "test_it_saves_path.ndjson"
    PolarsEagerNdJSON(path=path).save(df)
    assert pl.read_ndjson(path).equals(df)
