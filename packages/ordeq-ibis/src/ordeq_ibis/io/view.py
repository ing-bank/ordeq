from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

import ibis
from ibis import BaseBackend, Table
from ordeq import Output


@dataclass(frozen=True, kw_only=True)
class IbisView(Output[Table]):
    """IO to save to a view using Ibis.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisView
    >>> my_view_using_trino = IbisView(
    ...     name="my_view",
    ...     resource="trino://"
    ... )

    >>> my_view_using_duck_db = IbisView(
    ...     name="my_view",
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

    def save(self, t: Table, overwrite: bool = False) -> None:
        self._backend.create_view(self.name, t, overwrite=overwrite)
