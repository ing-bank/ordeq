from pathlib import Path

from ordeq import Input
from ordeq_files import Pickle
from ordeq_pandas import PandasCSV

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
)
columns = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width",
    "Labels",
]
csv_remote = PandasCSV(path=DATA_URL).with_load_options(names=columns)
csv_local = PandasCSV(path=Path("data/raw/iris_dataset.csv"))

csv_normalized = PandasCSV(
    path=Path("data/processed/normalized_iris_dataset.csv")
)
scaler = Input[str]("standard")

knn_model = Pickle(path=Path("data/models/knn_model.pkl"))
n_neighbors = Input[int](3)
seed = Input[int | None](0)
