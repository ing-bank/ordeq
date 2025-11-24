from typing import cast
from unittest.mock import MagicMock, patch

import pyiceberg.types as T
import pytest
from ordeq import IOException
from pyiceberg.catalog import CatalogType
from pyiceberg.catalog.memory import InMemoryCatalog

from ordeq_iceberg import IcebergCatalog, IcebergTableCreate, IfTableExistsSaveOptions


@pytest.fixture(scope="module")
def catalog_io() -> IcebergCatalog:
    return IcebergCatalog(name="test_catalog", catalog_type=CatalogType.IN_MEMORY)


@pytest.fixture(scope="module")
def catalog(catalog_io) -> InMemoryCatalog:
    catalog = cast(InMemoryCatalog, catalog_io.load())
    catalog.create_namespace("test_namespace")
    return catalog


def test_create_table(catalog: InMemoryCatalog):
    table_create = IcebergTableCreate(
        catalog=catalog,
        table_name="test_table",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    table_create.save(None)
    assert catalog.table_exists("test_namespace.test_table")


def test_create_table_with_catalog_io(sql_catalog_io: IcebergCatalog):
    catalog = sql_catalog_io.load()
    table_create = IcebergTableCreate(
        catalog=sql_catalog_io,
        table_name="test_table_io",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    table_create.save(None)
    assert catalog.table_exists("test_namespace.test_table_io")
    catalog.close()


def test_create_table_without_schema_raises(catalog: InMemoryCatalog):
    table_create = IcebergTableCreate(
        catalog=catalog,
        table_name="test_table_no_schema",
        namespace="test_namespace",
        schema=None,
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    with pytest.raises(IOException, match="Schema must be provided"):
        table_create.save(None)


def test_create_existing_table_raises(catalog: InMemoryCatalog):
    table_create = IcebergTableCreate(
        catalog=catalog,
        table_name="test_table_existing",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=IfTableExistsSaveOptions.RAISE,
    )
    table_create.save(None)
    with pytest.raises(
        IOException,
        match="Table 'test_namespace.test_table_existing' already exists",
    ):
        table_create.save(None)


def test_create_existing_table_ignore(catalog: InMemoryCatalog):
    table_create = IcebergTableCreate(
        catalog=catalog,
        table_name="test_table_no_action",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=IfTableExistsSaveOptions.IGNORE,
    )
    table_create.save(None)
    # Second save should do nothing and not raise
    table_create.save(None)
    assert catalog.table_exists("test_namespace.test_table_no_action")


def test_create_existing_table_drop(catalog: InMemoryCatalog):
    table_create = IcebergTableCreate(
        catalog=catalog,
        table_name="test_table_drop",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    table_create.save(None)
    # Second save should drop and recreate the table without raising
    table_create.save(None)
    assert catalog.table_exists("test_namespace.test_table_drop")


@patch("ordeq_iceberg.table_create.IcebergTableCreate._catalog_value")
@patch("ordeq_iceberg.table_create.IcebergTableCreate.table_exists")
def test_create_existing_table_if_exists_null(
    mock_table_exists: MagicMock, mock_catalog: MagicMock
):
    mock_table_exists.return_value = True
    table_create = IcebergTableCreate(
        catalog=mock_catalog,
        table_name="test_table_if_exists_null",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists=None,
    )
    table_create.save(None)
    mock_table_exists.assert_called_once()
    mock_catalog.create_table.assert_called_once()
