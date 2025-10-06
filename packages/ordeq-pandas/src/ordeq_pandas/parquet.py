from dataclasses import dataclass

import pandas as pd
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PandasParquet(IO[pd.DataFrame]):
    """IO to load from and save to PARQUET data using Pandas. Calls
    `pd.read_parquet` and `pd.write_parquet` under the hood.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasParquet
    >>> MyParquet = PandasParquet(
    ...     path=Path("path/to.parquet")
    ... )

    ```

    """

    path: PathLike

    def load(self, **load_options) -> pd.DataFrame:
        return pd.read_parquet(self.path, **load_options)

    def save(self, pdf: pd.DataFrame, **save_options) -> None:
        pdf.to_parquet(self.path, **save_options)
