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
    ...     name="my_catalog", catalog_type=CatalogType.IN_MEMORY
    ... )
    >>> catalog = iceberg_catalog.load()

    ```

    """

    name: str
    catalog_type: CatalogType | str

    def load(self, **load_options) -> Catalog:
        if isinstance(self.catalog_type, CatalogType):
            catalog_type_value = self.catalog_type.value
        else:
            catalog_type_value = str(self.catalog_type)
        return load_catalog(self.name, type=catalog_type_value, **load_options)
