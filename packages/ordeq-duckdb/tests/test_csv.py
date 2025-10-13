from pathlib import Path

import duckdb
from ordeq_duckdb import DuckDBCSV


def test_it_loads(connection: duckdb.DuckDBPyConnection, tmp_path: Path):
    path = tmp_path / "test_it_loads.csv"
    connection.values(["a", "apples", "green and red"]).to_csv(str(path))
    assert DuckDBCSV(path=str(path)).load().fetchall() == [
        ("a", "apples", "green and red")
    ]


def test_it_saves(tmp_path: Path):
    path = str(tmp_path / "test_it_saves.csv")
    data = ["a", "apples", "green and red"]
    relation = duckdb.values(data)
    DuckDBCSV(path=path).save(relation)
    assert duckdb.read_csv(path).fetchall() == [tuple(data)]
