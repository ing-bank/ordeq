from dataclasses import dataclass
from enum import StrEnum

from ordeq import Output
from pyiceberg.schema import Schema
from pyiceberg.types import StructType

from ordeq_iceberg.catalog import IcebergCatalog
from ordeq_iceberg.errors import IcebergTableAlreadyExistsError


class IfTableExistsSaveOptions(StrEnum):
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
    ...         NestedField(1, True, "id", IntegerType()),
    ...         NestedField(2, True, "name", StringType()),
    ...     ),
    ...     if_exists=IfTableExistsSaveOptions.DROP,
    ... )
    >>> table_create.save()
    ```

    If using for an Ordeq pipeline where you need to control both
    the creation and loading of the table, use this in
    combination with `IcebergTable` with a shared resource name.

    eg:

    ```pycon
    >>> from ordeq_iceberg import IcebergTable, IcebergTableCreate, IcebergCatalog
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
    ...         NestedField(1, True, "id", IntegerType()),
    ...         NestedField(2, True, "name", StringType()),
    ...     ),
    ...     if_exists=IfTableExistsSaveOptions.DROP,
    ... ) @ my_table_resource_name
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ... ) @ my_table_resource_name
    """

    catalog: IcebergCatalog
    table_name: str
    namespace: str
    schema: Schema | StructType
    """Schema to use when creating the table"""
    if_exists: IfTableExistsSaveOptions | None = None
    """What to do if the table already exists.
    None (default) lets the underlying catalog handle
    the situation (usually raises an error).
    """

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    def table_exists(self) -> bool:
        catalog = self.catalog.load()
        return catalog.table_exists(self.table_identifier)

    def save(self, _: None = None, **save_options) -> None:
        """Create the table in the catalog with the provided schema.

        Raises:
            ValueError: If the schema is not provided when creating a new table
            IcebergTableAlreadyExistsError: If the table already exists and
                `if_exists` is set to RAISE
        """
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
                case IfTableExistsSaveOptions.RAISE:
                    raise IcebergTableAlreadyExistsError(
                        f"Table '{self.table_identifier}' already exists."
                    )
        catalog.create_table(
            identifier=self.table_identifier, schema=schema, **save_options
        )
