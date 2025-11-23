from dataclasses import dataclass

from ordeq import Input
from pyiceberg.catalog import Catalog, CatalogType, load_catalog


@dataclass(frozen=True, kw_only=True)
class IcebergCatalog(Input[Catalog]):
    """IO for loading an Iceberg Catalog.

    Example:

    ```pycon
    >>> from pyiceberg.catalog import CatalogType
    >>> iceberg_catalog = IcebergCatalog(
    ...     name="my_catalog", catalog_type=CatalogType.HIVE
    ... )
    >>> catalog = iceberg_catalog.load()

    ```

    """

    name: str
    catalog_type: CatalogType | str

    def load(self, **load_options) -> Catalog:
        catalog_type_value = self.catalog_type
        if isinstance(self.catalog_type, CatalogType):
            catalog_type_value = self.catalog_type.value
        return load_catalog(self.name, type=catalog_type_value, **load_options)
