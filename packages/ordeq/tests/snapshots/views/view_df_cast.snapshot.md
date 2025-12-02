## Resource

```python
import pandas as pd
from ordeq import Input, node, run

dataframe = Input[pd.DataFrame](
    pd.DataFrame({
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "D": [2.0, 5.0, 8.0],
    })
)


@node(inputs=dataframe)
def df_casted(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


@node(inputs=df_casted)
def group_by(df: pd.DataFrame) -> None:
    print(
        df.groupby(by=["A"], as_index=False, dropna=False)
        .agg({"B": "mean", "D": "max"})
        .head()
    )


run(group_by, verbose=True)

```

## Output

```text
io-0 --> View:__main__:df_casted
View:__main__:df_casted --> io-1
io-1 --> View:__main__:group_by
View:__main__:group_by --> io-2
     A    B    D
0  bar  2.0  5.0
1  foo  2.0  8.0

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.runner	Running Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'df_casted:df' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'df_casted:df' in module '__main__'
DEBUG	ordeq.runner	Running view 'df_casted' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'group_by:df' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'group_by:df' in module '__main__'
DEBUG	ordeq.runner	Running view 'group_by' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'df_casted:df' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'group_by:df' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```