from ordeq import node, run
import duckdb
from ordeq_common import Literal

db = duckdb.connect(":memory:")
connection = Literal(db)


@node(inputs=connection)
def selected_range(conn: duckdb.DuckDBPyConnection) -> duckdb.DuckDBPyRelation:
    return conn.sql("SELECT * from range(3)")


@node(inputs=selected_range)
def range_to_csv(r: duckdb.DuckDBPyRelation) -> None:
    r.show()


run(range_to_csv, verbose=True)
