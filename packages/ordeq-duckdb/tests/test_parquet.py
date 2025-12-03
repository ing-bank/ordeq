from pathlib import Path

import duckdb
from ordeq_duckdb import DuckDBParquet


def test_it_loads(connection: duckdb.DuckDBPyConnection, tmp_path: Path):
    path = str(tmp_path / "test_it_loads.parquet")
    connection.values(["a", "apples", "green and red"]).to_parquet(path)
    assert DuckDBParquet(path=path).load().fetchall() == [
        ("a", "apples", "green and red")
    ]


def test_it_saves(tmp_path: Path):
    path = str(tmp_path / "test_it_saves.parquet")
    data = ["a", "apples", "green and red"]
    relation = duckdb.values(data)
    DuckDBParquet(path=path).save(relation)
    assert duckdb.read_parquet(path).fetchall() == [tuple(data)]
