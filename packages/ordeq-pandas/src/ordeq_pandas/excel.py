from dataclasses import dataclass

import pandas as pd
from ordeq.framework.io import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class PandasExcel(IO[pd.DataFrame]):
    """IO to load from and save to Excel data using Pandas. Calls
    `pd.read_excel` and `pd.to_excel` under the hood.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasExcel
    >>> MyExcel = PandasExcel(
    ...     path=Path("path/to.xlsx")
    ... ).load(usecols="A:C")  # doctest: +SKIP

    ```

    Load behaviour is configured by `with_load_options`:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasExcel
    >>> MyExcel = (
    ...     PandasExcel(
    ...         path=Path("path/to.xlsx")
    ...     )
    ...     .with_load_options(usecols="A:C")
    ... ).load()  # doctest: +SKIP

    ```
    """

    path: PathLike

    def load(self, **load_options) -> pd.DataFrame:
        return pd.read_excel(self.path, **load_options)

    def save(self, pdf: pd.DataFrame, **save_options) -> None:
        pdf.to_excel(self.path, **save_options)
