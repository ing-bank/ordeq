from ordeq import node, run
import pandas as pd
from ordeq_common import Literal

dataframe = Literal(
    pd.DataFrame(
        {
            "A": ["foo", "bar", "foo"],
            "B": [1, 2, 3],
            "C": ["one", "one", "two"],
            "D": [2.0, 5.0, 8.0],
        }
    )
)


@node(inputs=dataframe)
def df_casted(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


@node(inputs=df_casted)
def group_by(df: pd.DataFrame) -> None:
    print(df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"}).head())


run(group_by, verbose=True)
