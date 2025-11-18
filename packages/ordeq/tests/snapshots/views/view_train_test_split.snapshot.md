## Resource

```python
from typing import TypeAlias

import pandas as pd
from ordeq import node, run
from ordeq_common import Literal

dataframe = Literal(
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
NodeResourceGraph(nodes=2, resources=3, edges={View(name=__main__:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)]): [Resource(value=IO(id=ID1))], View(name=__main__:train, inputs=[IO(id=ID1)]): [Resource(value=IO(id=ID2))], Resource(value=Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)): [View(name=__main__:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])], Resource(value=IO(id=ID1)): [View(name=__main__:train, inputs=[IO(id=ID1)])], Resource(value=IO(id=ID2)): []})
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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:split'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:train'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.runner	Running view "split" in module "__main__"
INFO	ordeq.runner	Running view "train" in module "__main__"

```

## Typing

```text
packages/ordeq/tests/resources/views/view_train_test_split.py:25:12: error[invalid-return-type] Return type does not match returned value: expected `tuple[DataFrame, DataFrame]`, found `tuple[Series[Any], Series[Any]]`
Found 1 diagnostic

```