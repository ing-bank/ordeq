from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any

import ibis
from ibis import BaseBackend, Table
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class IbisTable(IO[Table]):
    """IO to load from and save to a table using Ibis.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisTable
    >>> my_table_using_polars = IbisTable(
    ...     name="my_table",
    ...     resource="polars://"
    ... )

    >>> my_table_using_duck_db = IbisTable(
    ...     name="my_table",
    ...     resource="duckdb://"
    ... )

    ```

    See [1] on how to configure the `resource`.

    [1]: https://ibis-project.org/reference/connection

    """

    name: str
    resource: Path | str

    @cached_property
    def _backend(self) -> BaseBackend:
        return ibis.connect(self.resource)

    def load(self) -> Table:
        return self._backend.table(self.name)

    def save(self, t: Table, **save_options: Any) -> None:
        self._backend.create_table(self.name, t, **save_options)
