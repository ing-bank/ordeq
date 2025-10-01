from pathlib import Path

from duckdb import DuckDBPyConnection
from ordeq_duckdb import DuckDBCSV, DuckDBTable


def test_it_loads(connection: DuckDBPyConnection, tmp_path: Path):
    path = tmp_path / "test_it_loads.csv"
    connection.values(["a", "apples", "green and red"]).to_csv(str(path))
    assert DuckDBCSV(path=str(path)).load().fetchall() == [
        ("a", "apples", "green and red")
    ]


def test_it_creates(connection: DuckDBPyConnection):
    relation = connection.sql("from range(2)")
    DuckDBTable(table="test_it_creates").save(relation)
    assert connection.table("test_it_creates").execute().fetchall() == [
        (0,),
        (1,),
    ]
