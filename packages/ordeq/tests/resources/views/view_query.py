import duckdb
from ordeq import Input, node, run

db = duckdb.connect(":memory:")
connection = Input(db)


@node(inputs=connection)
def selected_range(conn: duckdb.DuckDBPyConnection) -> duckdb.DuckDBPyRelation:
    return conn.sql("SELECT * from range(3)")


@node(inputs=selected_range)
def range_to_csv(r: duckdb.DuckDBPyRelation) -> None:
    r.show()


run(range_to_csv, verbose=True)
