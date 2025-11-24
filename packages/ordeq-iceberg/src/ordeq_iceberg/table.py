from dataclasses import dataclass

from ordeq import Input
from pyiceberg.catalog import Catalog
from pyiceberg.table import Table

from ordeq_iceberg.catalog import IcebergCatalog


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table]):
    """IO for loading an Iceberg table.

    Example:

    ```pycon
    >>> from ordeq_iceberg import IcebergTable, IcebergCatalog
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

    catalog: IcebergCatalog | Catalog
    table_name: str
    namespace: str

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    def load(self, **load_options) -> Table:
        """Load the table instance from the catalog

        Returns:
            The loaded Iceberg table instance
        """
        if isinstance(self.catalog, IcebergCatalog):
            catalog = self.catalog.load()
        else:
            catalog = self.catalog
        return catalog.load_table(self.table_identifier, **load_options)
