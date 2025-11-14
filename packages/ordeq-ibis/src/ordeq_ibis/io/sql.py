from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any

import ibis
from ibis import BaseBackend, Table
from ordeq import Input


@dataclass(frozen=True, kw_only=True)
class IbisSQL(Input[Table]):
    """IO to load a table from a sql expression using Ibis.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisSQL
    >>> my_sql_using_trino = IbisSQL(
    ...     query="SELECT * FROM my_table",
    ...     resource="trino://"
    ... )

    >>> my_sql_using_duck_db = IbisSQL(
    ...     query="SELECT * FROM my_table",
    ...     resource="duckdb://"
    ... )

    ```

    See [1] on how to configure the `resource`.

    [1]: https://ibis-project.org/reference/connection

    """

    query: str
    resource: Path | str

    @cached_property
    def _backend(self) -> BaseBackend:
        return ibis.connect(self.resource)

    def load(self, **load_options: Any) -> Table:
        return self._backend.sql(self.query, **load_options)  # type: ignore[attr-defined]
