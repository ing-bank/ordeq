import pandas as pd
from ordeq import node, run
from ordeq_common import Literal

dataframe = Literal(
    pd.DataFrame({
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "D": [2.0, 5.0, 8.0],
    })
)


@node(inputs=dataframe)
def df_selected(df: pd.DataFrame) -> pd.DataFrame:
    return df["A"].to_frame()


@node(inputs=df_selected)
def group_by(df: pd.DataFrame) -> None:
    print(
        df.groupby(by=["A"], as_index=False, dropna=False).agg("mean").head()
    )


run(group_by, verbose=True)
