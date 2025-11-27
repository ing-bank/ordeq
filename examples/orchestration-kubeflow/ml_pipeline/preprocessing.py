from typing import Literal

import pandas as pd
from ordeq import node
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from ml_pipeline import catalog


@node(inputs=catalog.csv_remote, outputs=catalog.csv_local)
def create_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Copies the remote iris dataset to a local CSV file."""
    return df


@node(
    inputs=[catalog.csv_local, catalog.scaler], outputs=catalog.csv_normalized
)
def normalize_dataset(
    df: pd.DataFrame, scaler: Literal["min_max", "standard"] | None = None
):
    labels = df.pop("Labels")

    match scaler:
        case "standard":
            scaler = StandardScaler()
        case "min_max":
            scaler = MinMaxScaler()
        case _:
            raise ValueError("Scaler must be either 'standard' or 'min_max'")

    df = pd.DataFrame(scaler.fit_transform(df))
    df["Labels"] = labels
    return df
