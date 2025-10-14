from ordeq import run
from ordeq import node
from ordeq import node as view
import pandas as pd
from ordeq_pandas import PandasDataFrame, PandasCSV

DataFrame = PandasDataFrame(
    data=(
        (1, 2, 3),
        (4.0, 5.5, 6.1),
        ("foo", "bar", "baz"),
        (True, False, True),
    ),
    columns=("A", "B", "C", "D"),
)


def filter_df(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    return df.where(condition)


first_df_casted = view(filter_df, inputs=DataFrame)
second_df_casted = view(filter_df, inputs=DataFrame)


@node(inputs=first_df_casted, outputs=PandasCSV(path="out.csv"))
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"})


print(run(group_by, verbose=True))
