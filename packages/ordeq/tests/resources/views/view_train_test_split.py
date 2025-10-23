from ordeq import node, run
from ordeq_common import Literal
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression

iris = Literal(load_iris())
model = Literal(LinearRegression())

Split = tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]


@node(inputs=iris)
def split(df: pd.DataFrame) -> Split:
    X, y = df['data'], df['target']
    return train_test_split(
        X, y, random_state=104, test_size=0.25, shuffle=True
    )


@node(inputs=split)
def train(data: Split) -> None:
    X_train, y_train, _, _ = data
    fitted = LinearRegression().fit(X_train, y_train)
    print(fitted.coef_)


print(run(train, verbose=True))
