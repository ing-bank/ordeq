from ordeq import node, run
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


@node(inputs=DataFrame)
def df_casted(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


@node(inputs=df_casted, outputs=PandasCSV(path="out.csv"))
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"})


print(run(group_by, verbose=True))
