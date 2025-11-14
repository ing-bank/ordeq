from pathlib import Path

import polars as pl
from ordeq_polars.lazy import PolarsLazyNdJSON


def test_it_loads_path(tmp_path: Path, lf: pl.LazyFrame):
    path = tmp_path / "test_it_loads_path.ndjson"
    lf.collect().write_ndjson(path)
    actual = PolarsLazyNdJSON(path=path).load().collect()
    assert actual.equals(lf.collect())
