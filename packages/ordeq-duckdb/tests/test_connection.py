from pathlib import Path

from ordeq_duckdb import DuckDBConnection


def test_it_loads(tmp_path: Path):
    connection = DuckDBConnection(database=":memory:").load()
    assert connection.execute("SELECT 1").fetchall() == [(1,)]
    # default is :memory:
    connection = DuckDBConnection().load()
    assert connection.execute("SELECT 2").fetchall() == [(2,)]
    # file path
    path = tmp_path / "test.duckdb"
    connection = DuckDBConnection(database=path).load()
    assert connection.execute("SELECT 3").fetchall() == [(3,)]
