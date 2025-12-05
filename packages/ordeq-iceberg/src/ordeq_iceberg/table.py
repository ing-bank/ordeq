from dataclasses import dataclass
from typing import Any

from ordeq import Input
from pyiceberg.catalog import Catalog
from pyiceberg.table import Table
from pyiceberg.typedef import Identifier


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table]):
    """IO for loading an Iceberg table.

    Example:

    ```pycon
    >>> import pyiceberg.types as T
    >>> from ordeq_iceberg import (
    ...     IcebergTable, IcebergCatalog
    ... )
    >>> catalog = IcebergCatalog(
    ...     name="my_catalog",
    ...     catalog_type="IN_MEMORY"
    ... )
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ... )

    ```

    """

    catalog: Input[Catalog] | Catalog
    table_name: str
    namespace: str

    @property
    def table_identifier(self) -> Identifier:
        return (self.namespace, self.table_name)

    @property
    def _catalog(self) -> Catalog:
        if isinstance(self.catalog, Input):
            return self.catalog.load()  # type: ignore[return-value]
        return self.catalog

    def load(self, **load_options: Any) -> Table:
        """Load the table instance from the catalog

        Returns:
            The loaded Iceberg table instance
        """
        return self._catalog.load_table(self.table_identifier, **load_options)
