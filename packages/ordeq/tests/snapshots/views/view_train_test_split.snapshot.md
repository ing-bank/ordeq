## Resource

```python
from typing import TypeAlias

import pandas as pd
from ordeq import Input, node, run

dataframe = Input[pd.DataFrame](
    pd.DataFrame({
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "gt": [2.0, 5.0, 8.0],
    })
)

Split: TypeAlias = tuple[pd.DataFrame, pd.DataFrame]


@node(inputs=dataframe)
def split(df: pd.DataFrame) -> Split:
    df = df.sample(frac=1, random_state=1).reset_index(drop=True)
    n_test = int(len(df) * 0.25)
    test_df = df.iloc[:n_test]
    train_df = df.iloc[n_test:]
    return train_df, test_df


@node(inputs=split)
def train(data: Split) -> None:
    # Put your training code here
    print("Training", data[0].describe())


run(train, verbose=True)

```

## Output

```text
io-0 --> View:__main__:split
View:__main__:split --> io-1
io-1 --> View:__main__:train
View:__main__:train --> io-4
Training          B   gt
count  3.0  3.0
mean   2.0  5.0
std    1.0  3.0
min    1.0  2.0
25%    1.5  3.5
50%    2.0  5.0
75%    2.5  6.5
max    3.0  8.0

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input 'split:df' in module '__main__'
INFO	ordeq.runner	Running view 'split' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'train:data' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'train:data' in module '__main__'
INFO	ordeq.runner	Running view 'train' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'train:data' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```