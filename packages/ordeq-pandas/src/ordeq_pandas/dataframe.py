from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

import pandas as pd
from ordeq import Input


@dataclass(frozen=True, kw_only=True)
class PandasDataFrame(Input[pd.DataFrame]):
    """Allows a Pandas DataFrame to be hard-coded in Python. This is suitable
    for small tables such as simple dimension tables that are unlikely to
    change. It is also useful for unit testing.

    Example usage:

    ```pycon
    >>> from ordeq_pandas import PandasDataFrame
    >>> df = PandasDataFrame(
    ...     columns=["year", "datafile"],
    ...     data=[
    ...         (2022, "file_2022.xlsx"),
    ...         (2023, "file_2023.xlsx"),
    ...         (2024, "file_2024.xlsx"),
    ...     ]
    ... ).load()
    >>> print(df.shape)
    (3, 2)

    ```

    """

    data: Iterable[tuple[Any, ...]]
    columns: list[str] | None = None

    def load(self, **load_options: Any) -> pd.DataFrame:
        """Loads the DataFrame from the provided data and columns.

        Args:
            **load_options: Additional options passed to `pd.DataFrame`.

        Returns:
            Loaded Pandas DataFrame.
        """

        return pd.DataFrame(data=self.data, columns=self.columns, **load_options)
