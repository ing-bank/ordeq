from ordeq import node
from ordeq._nodes import get_node
import pandas as pd
from ordeq_common import Print

DataFrame = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4.0, 5.5, 6.1],
        "C": ["foo", "bar", "baz"],
        "D": [True, False, True],
    }
)


@node(inputs=DataFrame)
def view(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


@node(inputs=view, outputs=Print())
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"})


print(repr(get_node(view)))
print(repr(get_node(n)))
