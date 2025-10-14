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


def cast(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


# For standalone usage, I find using the 'node' function a bit.
# I'd prefer calling 'view' instead:
df_casted = node(cast, inputs=DataFrame)  # awkward, imo
df_casted = view(cast, inputs=DataFrame)  # better
# or even
df_casted = view(cast, DataFrame)  # better


@node(inputs=df_casted, outputs=PandasCSV(path="out.csv"))
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"})


print(run(group_by, verbose=True))
