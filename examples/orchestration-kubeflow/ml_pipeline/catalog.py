from pathlib import Path

from ordeq import Input
from ordeq_files import Pickle
from ordeq_pandas import PandasCSV

csv_remote = PandasCSV(
    path="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
).with_load_options(
    names=[
        "Sepal_Length",
        "Sepal_Width",
        "Petal_Length",
        "Petal_Width",
        "Labels",
    ]
)
csv_local = PandasCSV(path="iris_dataset.csv")
csv_normalized = PandasCSV(path="normalized_iris_dataset.csv")
scaler = Input[str]("standard")

knn_model = Pickle(path=Path("knn_model.pkl"))
n_neighbors = Input[int](3)
seed = Input[int | None](0)
