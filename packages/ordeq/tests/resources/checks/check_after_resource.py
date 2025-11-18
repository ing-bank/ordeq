import tempfile
from pathlib import Path

import pandas as pd
import polars as pl
from ordeq import node, run
from ordeq_pandas import PandasCSV
from ordeq_polars import PolarsEagerCSV
from ordeq_viz import viz

csv = Path(tempfile.mkdtemp()) / "my.csv"
csv_pandas = PandasCSV(path=csv) @ csv
csv_polars = PolarsEagerCSV(path=csv) @ csv


@node(inputs=csv_polars, checks=csv)
def check(data: pl.DataFrame):
    print(data.head())


@node(outputs=csv_pandas)
def produce() -> pd.DataFrame:
    return pd.DataFrame({"hello": [1, 2, 3], "world": ["A", "B", "C"]})


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)
