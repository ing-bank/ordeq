from ordeq import node, run
from ordeq_duckdb import DuckDBCSV
import duckdb
from ordeq_common import Literal

db = duckdb.connect(":memory:")
connection = Literal(db)


@node(inputs=connection)
def selected_range(conn: duckdb.DuckDBPyConnection) -> duckdb.DuckDBPyRelation:
    return conn.sql("SELECT * from range(3)")


@node(inputs=selected_range, outputs=DuckDBCSV(path="my-path.csv"))
def range_to_csv(range: duckdb.DuckDBPyRelation) -> duckdb.DuckDBPyRelation:
    return range


print(run(range_to_csv, verbose=True))
