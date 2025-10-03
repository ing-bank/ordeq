from dataclasses import dataclass

import pandas as pd
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PandasCSV(IO[pd.DataFrame]):
    """IO to load from and save to CSV data using Pandas. Calls
    `pd.read_csv` and `pd.write_csv` under the hood.

    Example:

    ```python
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasCSV
    >>> csv = PandasCSV(
    ...     path=Path("path/to.csv")
    ... ).load(header="infer")  # doctest: +SKIP

    ```

    Load behaviour is configured by `with_load_options`:

    ```python
    >>> csv = PandasCSV(
    ...     path=Path("path/to.csv")
    ... ).with_load_options(header="infer")

    ```

    Save behaviour is configured by `with_save_options`:

    ```python
    >>> csv = PandasCSV(
    ...     path=Path("path/to.csv"),
    ... ).with_save_options(header=True)

    ```

    """

    path: PathLike | str

    def load(self, **load_options) -> pd.DataFrame:
        return pd.read_csv(self.path, **load_options)

    def save(self, pdf: pd.DataFrame, **save_options) -> None:
        pdf.to_csv(self.path, **save_options)
