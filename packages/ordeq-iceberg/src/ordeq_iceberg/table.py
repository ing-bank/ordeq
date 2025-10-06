from dataclasses import dataclass
from enum import StrEnum

from ordeq.framework.io import Input, Output, _IOMeta  # noqa: PLC2701
from pyiceberg.catalog import Catalog
from pyiceberg.catalog.glue import GlueCatalog
from pyiceberg.catalog.memory import InMemoryCatalog
from pyiceberg.schema import Schema
from pyiceberg.table import Table
from pyiceberg.types import StructType


class IfTableExistsSaveOptions(StrEnum):
    """Options for handling existing tables when saving."""

    DROP = "drop"
    """Drop the existing table before creating a new one."""
    IGNORE = "ignore"
    """Do nothing if the table already exists."""


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table], Output[None], metaclass=_IOMeta):
    """IO for loading an Iceberg table.

    Example:

    ```python
    >>> from ordeq_iceberg import IcebergTable, IcebergGlueCatalog
    >>> from pathlib import Path
    >>> catalog = IcebergGlueCatalog(
    ...     name="my_catalog"
    ... )
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace"
    ... )

    ```

    """

    catalog: Input[Catalog | GlueCatalog | InMemoryCatalog]
    table_name: str
    namespace: str
    schema: Schema | StructType | None = None
    """Schema to use when creating a new table. Required for saving"""
    if_exists: IfTableExistsSaveOptions | None = None
    """What to do if the table already exists when saving.
    By default, an error is raised.
    """

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
        print(f"Loading Iceberg table '{self.table_identifier}'...")
        catalog = self.catalog.load()
        return catalog.load_table(self.table_identifier, **load_options)

    def save(self, _: None = None, **save_options) -> None:
        """Create the table in the catalog with the provided schema.

        Raises:
            ValueError: If the schema is not provided when creating a new table
        """
        print(f"Saving Iceberg table '{self.table_identifier}'...")
        catalog = self.catalog.load()
        schema = self.schema or save_options.pop("schema", None)
        if schema is None:
            raise ValueError("Schema must be provided to create a new table.")
        if isinstance(schema, StructType):
            schema = Schema(*schema.fields)
        table_exists = self.table_exists()
        if table_exists:
            match self.if_exists:
                case IfTableExistsSaveOptions.IGNORE:
                    return
                case IfTableExistsSaveOptions.DROP:
                    catalog.drop_table(self.table_identifier)
        catalog.create_table(
            identifier=self.table_identifier, schema=schema, **save_options
        )
