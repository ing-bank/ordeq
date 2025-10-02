import duckdb
import pytest
from ordeq import IOException
from ordeq_duckdb import DuckDBView


def test_it_loads(connection: duckdb.DuckDBPyConnection):
    connection.values(["a", "apples", "green and red"]).to_view(
        "test_it_loads"
    )
    view = DuckDBView("test_it_loads", connection=connection).load()
    assert view.fetchall() == [("a", "apples", "green and red")]


def test_it_replaces(connection: duckdb.DuckDBPyConnection):
    relation = connection.sql("from range(2)")
    DuckDBView("test_it_saves", connection=connection).save(relation)
    view = connection.view("test_it_saves").execute()
    assert view.fetchall() == [(0,), (1,)]


def test_it_creates(connection: duckdb.DuckDBPyConnection):
    relation = connection.sql("from range(2)")
    relation.create_view("test_it_saves")
    with pytest.raises(IOException, match="already exists"):
        DuckDBView("test_it_saves", connection=connection).save(
            relation, replace=False
        )
