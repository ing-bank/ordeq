from dataclasses import dataclass

from ordeq import Input
from pyiceberg.catalog.glue import GlueCatalog
from pyiceberg.catalog.memory import InMemoryCatalog


@dataclass(frozen=True, kw_only=True)
class IcebergGlueCatalog(Input[GlueCatalog]):
    """IO for loading an AWS Glue Catalog for Iceberg tables."""

    name: str

    def load(self, **load_options) -> GlueCatalog:
        return GlueCatalog(name=self.name, **load_options)


@dataclass(frozen=True, kw_only=True)
class IcebergInMemoryCatalog(Input[InMemoryCatalog]):
    """IO for loading an in-memory Catalog for Iceberg tables."""

    name: str

    def load(self, **load_options) -> InMemoryCatalog:
        return InMemoryCatalog(name=self.name, **load_options)
