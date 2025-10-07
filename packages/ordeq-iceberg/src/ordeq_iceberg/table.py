from dataclasses import dataclass
from enum import StrEnum

from ordeq.framework.io import Input, Output
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
    ERROR = "error"
    """Raise an error if the table already exists."""


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table]):
    """IO for loading an Iceberg table.

    Example:

    ```python
    >>> from ordeq_iceberg import IcebergTable, IcebergGlueCatalog
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

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    def load(self, **load_options) -> Table:
        """Load the table instance from the catalog

        Returns:
            Table: The loaded Iceberg table instance
        """
        print(f"Loading Iceberg table '{self.table_identifier}'...")
        catalog = self.catalog.load()
        return catalog.load_table(self.table_identifier, **load_options)


@dataclass(frozen=True, kw_only=True)
class IcebergTableCreate(Output[None]):
    """IO for saving (creating) an Iceberg table in a catalog.

    This IO creates a new table in the specified catalog with the provided
    schema, without any input data.

    Example:
    ```python
    >>> from ordeq_iceberg import IcebergTableCreate, IcebergGlueCatalog
    >>> from pyiceberg.schema import Schema
    >>> from pyiceberg.types import NestedField, IntegerType, StringType
    >>> catalog = IcebergGlueCatalog(
    ...     name="my_catalog"
    ... )
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace"
    ... )
    >>> table_create = IcebergTableCreate(
    ...     table=table,
    ...     schema=Schema(
    ...         NestedField(1, "id", IntegerType(), required=True),
    ...         NestedField(2, "data", StringType(), required=False),
    ...     ),
    ...     if_exists="drop"  # Options: None, "error", "drop", "ignore"
    ... )

    ```
    """

    table: IcebergTable
    """IcebergTable Input object defining the table to create."""
    schema: Schema | StructType
    """Schema to use when creating the table"""
    if_exists: IfTableExistsSaveOptions | None = None
    """What to do if the table already exists when saving.
    By default, an error is raised.
    """

    def save(self, _: None = None, **save_options) -> None:
        """Create the table in the catalog with the provided schema."""
        print(f"Saving Iceberg table '{self.table.table_identifier}'...")
        loaded_catalog = self.table.catalog.load()
        schema = self.schema or save_options.pop("schema", None)
        if isinstance(schema, StructType):
            schema = Schema(*schema.fields)
        table_identifier = self.table.table_identifier
        table_exists = loaded_catalog.table_exists(table_identifier)
        if table_exists:
            match self.if_exists:
                case IfTableExistsSaveOptions.IGNORE:
                    return
                case IfTableExistsSaveOptions.DROP:
                    loaded_catalog.drop_table(table_identifier)
        loaded_catalog.create_table(
            identifier=table_identifier, schema=schema, **save_options
        )
