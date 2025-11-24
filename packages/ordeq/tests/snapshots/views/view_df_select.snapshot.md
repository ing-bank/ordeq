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
def df_selected(df: pd.DataFrame) -> pd.DataFrame:
    return df["A"].to_frame()


@node(inputs=df_selected)
def group_by(df: pd.DataFrame) -> None:
    print(
        df.groupby(by=["A"], as_index=False, dropna=False).agg("mean").head()
    )


run(group_by, verbose=True)

```

## Output

```text
io-0 --> View:__main__:df_selected
View:__main__:df_selected --> io-1
io-1 --> View:__main__:group_by
View:__main__:group_by --> io-2
     A
0  bar
1  foo

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view 'df_selected' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running view 'group_by' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```