from ordeq import node, run, view
from ordeq_common import Literal
import duckdb
import pandas as pd

csv = Literal(duckdb.values((1, 2, 3)))


@view(inputs=csv)
def csv_as_df(data: duckdb.DuckDBPyRelation) -> pd.DataFrame:
    return data.to_df()


@node(inputs=csv_as_df)
def aggregate(df: pd.DataFrame) -> None:
    df.aggregate("sum").head()


print(run(aggregate, verbose=True))
