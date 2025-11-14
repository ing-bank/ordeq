from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any

import ibis
from ibis import BaseBackend, Table
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class IbisParquet(IO[Table]):
    """IO to load from and save to PARQUET data using Ibis.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisParquet
    >>> my_parquet_using_polars = IbisParquet(
    ...     path=Path("path/to.parquet"),
    ...     resource="polars://"
    ... )

    >>> my_parquet_using_duck_db = IbisParquet(
    ...     path=Path("path/to.parquet"),
    ...     resource="duckdb://"
    ... )

    ```

    See [1] on how to configure the `resource`.

    [1]: https://ibis-project.org/reference/connection

    """

    path: Path
    resource: Path | str

    @cached_property
    def _backend(self) -> BaseBackend:
        return ibis.connect(self.resource)

    def load(self, **load_options: Any) -> Table:
        return self._backend.read_parquet(self.path, **load_options)

    def save(self, t: Table, **save_options: Any) -> None:
        self._backend.to_parquet(t, self.path, **save_options)
