from dataclasses import dataclass

from ordeq import Input
from pyiceberg.table import Table

from ordeq_iceberg.catalog import IcebergCatalog


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table]):
    """IO for loading an Iceberg table.

    Example:

    ```pycon
    >>> from ordeq_iceberg import IcebergTable, IcebergCatalog
    >>> from pathlib import Path
    >>> catalog = IcebergCatalog(
    ...     name="my_catalog",
    ...     catalog_type="IN_MEMORY"
    ... )
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace"
    ... )

    ```

    """

    catalog: IcebergCatalog
    table_name: str
    namespace: str

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    def table_exists(self) -> bool:
        catalog = self.catalog.load()
        return catalog.table_exists(self.table_identifier)

    def load(self, **load_options) -> Table:
        """Load the table instance from the catalog

        Returns:
            Table: The loaded Iceberg table instance
        """
        catalog = self.catalog.load()
        return catalog.load_table(self.table_identifier, **load_options)
