import duckdb
import pytest
from ordeq import IOException
from ordeq_duckdb import DuckDBTable


def test_it_loads(connection: duckdb.DuckDBPyConnection):
    relation = connection.sql("from range(3)")
    relation.to_table("test_it_loads")
    assert DuckDBTable(
        table="test_it_loads", connection=connection
    ).load().fetchall() == [(0,), (1,), (2,)]


def test_it_loads_with_default_connection():
    table = DuckDBTable(table="test_it_loads_with_default_connection")
    relation = table.connection.sql("from range(3)")
    relation.to_table("test_it_loads_with_default_connection")
    assert table.load().fetchall() == [(0,), (1,), (2,)]


def test_it_creates(connection: duckdb.DuckDBPyConnection):
    relation = connection.sql("from range(2)")
    DuckDBTable(table="test_it_creates").save(relation)
    assert connection.table("test_it_creates").execute().fetchall() == [
        (0,),
        (1,),
    ]


def test_it_raises_error_if_table_exists(
    connection: duckdb.DuckDBPyConnection,
):
    relation = connection.sql("from range(2)")
    table = "test_it_raises_error_if_table_exists"
    relation.create(table)
    table = DuckDBTable(table=table)
    with pytest.raises(IOException, match="already exists"):
        table.save(relation)


def test_it_inserts(connection: duckdb.DuckDBPyConnection):
    relation = connection.sql("from range(2)")
    table = DuckDBTable(table="test_it_inserts").with_save_options(
        mode="insert"
    )
    table.save(relation)
    table.save(relation)
    assert connection.table("test_it_inserts").execute().fetchall() == [
        (0,),
        (1,),
        (0,),
        (1,),
    ]
