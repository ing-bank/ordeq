from dataclasses import dataclass
from enum import Enum

from ordeq import Input, Output
from pyiceberg.catalog import Catalog
from pyiceberg.schema import Schema
from pyiceberg.types import StructType

from ordeq_iceberg.errors import IcebergTableAlreadyExistsError


class IfTableExistsSaveOptions(Enum):
    """Options for handling existing tables when saving."""

    DROP = "drop"
    """Drop the existing table before creating a new one."""
    IGNORE = "ignore"
    """Do nothing if the table already exists."""
    RAISE = "raise"
    """Raise an error if the table already exists."""


@dataclass(frozen=True, kw_only=True)
class IcebergTableCreate(Output[None]):
    """Ordeq output for creating an Iceberg table.

    Example:

    ```pycon
    >>> from ordeq_iceberg import IcebergTableCreate, IcebergCatalog
    >>> from pyiceberg.schema import Schema, NestedField
    >>> from pyiceberg.catalog import CatalogType
    >>> from pyiceberg.types import StringType, IntegerType
    >>> catalog = IcebergCatalog(
    ...     name="my_catalog", catalog_type=CatalogType.IN_MEMORY
    ... )
    >>> table_create = IcebergTableCreate(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ...     schema=Schema(
    ...         NestedField(
    ...            field_id=1,
    ...            required=True,
    ...            name="id",
    ...            field_type=IntegerType()
    ...        ),
    ...         NestedField(
    ...            field_id=2,
    ...            required=True,
    ...            name="name",
    ...            field_type=StringType()
    ...        ),
    ...     ),
    ...     if_exists=IfTableExistsSaveOptions.DROP,
    ... )

    ```

    If using for an Ordeq pipeline where you need to control both
    the creation and loading of the table, use this in
    combination with `IcebergTable` with a shared resource name.

    eg:

    ```pycon
    >>> from ordeq_iceberg import (
    ...     IcebergTableCreate,
    ...     IcebergTable,
    ...     IcebergCatalog,
    ...     IfTableExistsSaveOptions,
    ... )
    >>> from pyiceberg.schema import Schema, NestedField
    >>> from pyiceberg.catalog import CatalogType
    >>> from pyiceberg.types import StringType, IntegerType
    >>> catalog = IcebergCatalog(
    ...     name="my_catalog", catalog_type=CatalogType.IN_MEMORY
    ... )
    >>> my_table_resource_name = "my_table.my_namespace"
    >>> table_create = IcebergTableCreate(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ...     schema=Schema(
    ...         NestedField(
    ...            field_id=1,
    ...            required=True,
    ...            name="id",
    ...            field_type=IntegerType()
    ...        ),
    ...         NestedField(
    ...            field_id=2,
    ...            required=True,
    ...            name="name",
    ...            field_type=StringType()
    ...        ),
    ...     ),
    ...     if_exists=IfTableExistsSaveOptions.DROP,
    ... ) @ my_table_resource_name
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ... ) @ my_table_resource_name
    """

    catalog: Input[Catalog] | Catalog
    table_name: str
    namespace: str
    schema: Schema | StructType
    """Schema to use when creating the table"""
    if_exists: IfTableExistsSaveOptions | str | None = None
    """What to do if the table already exists.
    None (default) lets the underlying catalog handle
    the situation (usually raises an error).
    """

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    @property
    def _catalog_value(self) -> Catalog:
        if isinstance(self.catalog, Input):
            return self.catalog.load()
        return self.catalog

    @property
    def _schema_value(self) -> Schema:
        if isinstance(self.schema, StructType):
            return Schema(*self.schema.fields)
        return self.schema

    def table_exists(self) -> bool:
        catalog = self._catalog_value
        return catalog.table_exists(self.table_identifier)

    def save(self, _: None = None, **save_options) -> None:
        """Create the table in the catalog with the provided schema.

        Raises:
            IcebergTableAlreadyExistsError: If the table already exists and
                `if_exists` is set to RAISE
        """
        catalog = self._catalog_value
        table_exists = self.table_exists()
        if table_exists:
            match self.if_exists:
                case (
                    IfTableExistsSaveOptions.IGNORE
                    | IfTableExistsSaveOptions.IGNORE.value
                ):
                    return
                case (
                    IfTableExistsSaveOptions.DROP
                    | IfTableExistsSaveOptions.DROP.value
                ):
                    catalog.drop_table(self.table_identifier)
                case (
                    IfTableExistsSaveOptions.RAISE
                    | IfTableExistsSaveOptions.RAISE.value
                ):
                    raise IcebergTableAlreadyExistsError(
                        f"Table '{self.table_identifier}' already exists."
                    )
        catalog.create_table(
            identifier=self.table_identifier,
            schema=self._schema_value,
            **save_options,
        )
