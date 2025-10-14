from ordeq import node, run
from ordeq_duckdb import DuckDBCSV
from ordeq_common import Print
import duckdb
import pandas as pd

csv = DuckDBCSV(path="my.csv")


@node(inputs=csv)
def csv_as_df(data: duckdb.DuckDBPyRelation) -> pd.DataFrame:
    return data.to_df()


@node(inputs=csv_as_df, outputs=Print())
def aggregate(df: pd.DataFrame) -> float:
    return df["A"].aggregate("sum")


print(run(aggregate, verbose=True))
