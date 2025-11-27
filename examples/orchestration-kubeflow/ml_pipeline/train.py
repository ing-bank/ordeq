import pandas as pd
from ordeq import node
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from ml_pipeline import catalog


@node(
    inputs=[catalog.csv_normalized, catalog.n_neighbors, catalog.seed],
    outputs=catalog.knn_model,
)
def train_model(
    df: pd.DataFrame, n_neighbors: int, seed: int | None = None
) -> BaseEstimator:
    y = df.pop("Labels")
    X = df

    X_train, _X_test, y_train, _y_test = train_test_split(
        X, y, random_state=seed
    )

    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    return clf
