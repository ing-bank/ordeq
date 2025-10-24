from ordeq import node, run
import pandas as pd
from ordeq import Output
from ordeq_common import Literal

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "D": [2.0, 5.0, 8.0],
    }
)

dataframe = Literal(df)

fltr = Literal(df["B"] > 4)


def filter_df(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    return df.where(condition)


df_filtered = node(filter_df, inputs=[dataframe, fltr])


class PandasHead(Output[pd.DataFrame]):
    def save(self, df: pd.DataFrame) -> None:
        print(df.head())


@node(inputs=df_filtered)
def group_by(df: pd.DataFrame) -> None:
    print(df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg(
        {"B": "mean", "D": "max"}
    ).head())


print(run(group_by, verbose=True))
