from ordeq import node, run
import pandas as pd
from ordeq_pandas import PandasDataFrame
from ordeq_common import Print

DataFrame = PandasDataFrame(
    data=(
        (1, 2, 2),
        (4.0, 5.5, 6.1),
        ("foo", "bar", "baz"),
        (True, False, True),
    ),
    columns=("A", "B", "C", "D"),
)


@node(inputs=DataFrame)
def df_selected(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["A", "B"]]


@node(inputs=df_selected, outputs=Print())
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"A": "mean"})


print(run(group_by, verbose=True))
