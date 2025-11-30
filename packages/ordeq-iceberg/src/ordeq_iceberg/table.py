from dataclasses import dataclass
from enum import Enum

from ordeq import Input, Output
from pyiceberg.catalog import Catalog
from pyiceberg.schema import Schema
from pyiceberg.table import Table
from pyiceberg.types import StructType

from ordeq_iceberg.errors import IcebergIOError, IcebergTableAlreadyExistsError


class IfTableExistsSaveOptions(Enum):
    """Options for handling existing tables when saving."""

    DROP = "drop"
    """Drop the existing table before creating a new one."""
    IGNORE = "ignore"
    """Do nothing if the table already exists."""
    RAISE = "raise"
    """Raise an error if the table already exists."""


@dataclass(frozen=True, kw_only=True)
class IcebergTable(Input[Table], Output[None]):
    """IO for loading an Iceberg table.

    Example:

    ```pycon
    >>> import pyiceberg.types as T
    >>> from ordeq_iceberg import (
    ...     IcebergTable, IcebergCatalog, IfTableExistsSaveOptions
    ... )
    >>> catalog = IcebergCatalog(
    ...     name="my_catalog",
    ...     catalog_type="IN_MEMORY"
    ... )
    >>> table = IcebergTable(
    ...     catalog=catalog,
    ...     table_name="my_table",
    ...     namespace="my_namespace",
    ...     schema=T.StructType(
    ...         T.NestedField(1, "id", T.IntegerType(), required=True),
    ...         T.NestedField(2, "data", T.StringType(), required=False),
    ...     ),
    ...     if_exists=IfTableExistsSaveOptions.DROP,
    ... )

    ```

    """

    catalog: Input[Catalog] | Catalog
    table_name: str
    namespace: str
    schema: Schema | StructType | None = None
    """Schema to use when creating the table. Required when saving"""
    if_exists: IfTableExistsSaveOptions | str | None = None
    """What to do if the table already exists when saving.
    None (default) lets the underlying catalog handle
    the situation (usually raises an error).
    """

    @property
    def table_identifier(self) -> str:
        return f"{self.namespace}.{self.table_name}"

    @property
    def _catalog_value(self) -> Catalog:
        if isinstance(self.catalog, Input):
            return self.catalog.load()  # type: ignore[return-value]
        return self.catalog

    @property
    def _schema_value(self) -> Schema | None:
        if not self.schema:
            return None
        if isinstance(self.schema, StructType):
            return Schema(*self.schema.fields)
        return self.schema

    def table_exists(self) -> bool:
        catalog = self._catalog_value
        return catalog.table_exists(self.table_identifier)

    def persist(self, _) -> None:
        """Don't persist the table, since it returns
        different types when loading and saving."""

    def load(self, **load_options) -> Table:
        """Load the table instance from the catalog

        Returns:
            The loaded Iceberg table instance
        """
        catalog = self._catalog_value
        return catalog.load_table(self.table_identifier, **load_options)

    def save(self, _: None = None, **save_options) -> None:
        """Create the table in the catalog with the provided schema.

        Raises:
            IcebergIOError:
                If the schema is not provided when saving a new table.
            IcebergTableAlreadyExistsError: If the table already exists and
                `if_exists` is set to RAISE
        """
        catalog = self._catalog_value
        table_exists = self.table_exists()
        schema = self._schema_value or save_options.get("schema")
        if not schema:
            raise IcebergIOError(
                "Schema must be provided when saving a new Iceberg table."
            )
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
