from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Any

import ibis
from ibis import BaseBackend, Table
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class IbisXlsx(IO[Table]):
    """IO to load from and save to XLSX data using Ibis.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisXlsx
    >>> my_xlsx_using_polars = IbisXlsx(
    ...     path=Path("path/to.xlsx"),
    ...     resource="polars://"
    ... )

    >>> my_xlsx_using_duck_db = IbisXlsx(
    ...     path=Path("path/to.xlsx"),
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
        return self._backend.read_xlsx(self.path, **load_options)  # type: ignore[attr-defined]

    def save(self, t: Table, header: bool = True, **save_options: Any) -> None:
        self._backend.to_xlsx(t, self.path, header=header, **save_options)  # type: ignore[attr-defined]
