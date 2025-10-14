from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

import pandas as pd
from ordeq import Input
from pandas import Index


@dataclass(frozen=True, kw_only=True)
class PandasDataFrame(Input[pd.DataFrame]):
    """Allows a Pandas DataFrame to be hard-coded as IO. This is suitable
    for small tables such as simple dimension tables that are unlikely to
    change. It is also useful for unit testing.

    Example usage:

    ```pycon
    >>> from ordeq_pandas import PandasDataFrame
    >>> df = PandasDataFrame(
    ...     data=(
    ...         (2022, "file_2022.xlsx"),
    ...         (2023, "file_2023.xlsx"),
    ...         (2024, "file_2024.xlsx"),
    ...     ),
    ...     columns=("year", "datafile"),
    ... ).load()
    >>> print(df.shape)
    (3, 2)

    ```

    """

    _idx: str = field(
        init=False, default_factory=lambda: str(uuid4()), repr=False
    )
    data: Iterable = field(hash=False)
    columns: Index | Iterable[str] | None = field(hash=False, default=None)

    def load(self, **load_options: Any) -> pd.DataFrame:
        """Loads the DataFrame from the provided data and columns.

        Args:
            **load_options: Additional options passed to `pd.DataFrame`.

        Returns:
            Loaded Pandas DataFrame.
        """

        return pd.DataFrame(
            data=self.data,
            columns=self.columns,  # type: ignore[arg-type]
            **load_options
        )
