from ordeq import node, run, view
import pandas as pd
from ordeq_common import Literal

dataframe = Literal(
    pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": [1, 2, 3, 4, 5, 6, 7, 8],
            "C": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "D": [2.0, 5.0, 8.0, 1.0, 2.0, 9.0, 3.0, 4.0],
        }
    )
)


@view(inputs=dataframe)
def df_selected(df: pd.DataFrame) -> pd.DataFrame:
    return df["A"].to_frame()


@node(inputs=df_selected)
def group_by(df: pd.DataFrame) -> None:
    df.groupby(
        by=["A"],
        as_index=False,
        dropna=False,
    ).agg("mean").head()


print(run(group_by, verbose=True))
