## Resource

```python
from ordeq import node, run
from ordeq_common import Literal
import pandas as pd

dataframe = Literal(
    pd.DataFrame(
        {
            "A": ["foo", "bar", "foo"],
            "B": [1, 2, 3],
            "C": ["one", "one", "two"],
            "gt": [2.0, 5.0, 8.0],
        }
    )
)

Split = tuple[pd.DataFrame, pd.DataFrame]


@node(inputs=dataframe)
def split(df: pd.DataFrame) -> Split:
    df = df.sample(frac=1, random_state=1).reset_index(
        drop=True
    )
    n_test = int(len(df) * 0.25)
    test_df = df.iloc[:n_test]
    train_df = df.iloc[n_test:]
    return train_df, test_df


@node(inputs=split)
def train(data: Split) -> None:
    # Put your training code here
    print('Training', data[0].describe())


print(run(train, verbose=True))

```

## Exception

```text
CycleError: ('nodes are in a cycle', [View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)]), View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])
```

## Output

```text
NodeGraph:
  Edges:
     view_train_test_split:split -> [view_train_test_split:split]
     view_train_test_split:train -> []
  Nodes:
     View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
     View(name=view_train_test_split:train, inputs=[View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_train_test_split:split'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_train_test_split:train'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```