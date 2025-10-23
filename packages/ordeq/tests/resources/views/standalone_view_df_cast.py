from ordeq import node, run
from ordeq import Output
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


def cast(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


df_casted = node(cast, inputs=dataframe)


class PandasHead(Output[pd.DataFrame]):
    def save(self, df: pd.DataFrame) -> None:
        print(df.head())


@node(inputs=df_casted, outputs=PandasHead())
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"})


print(run(group_by, verbose=True))
