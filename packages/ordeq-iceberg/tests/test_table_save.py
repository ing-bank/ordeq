from typing import cast
from unittest.mock import MagicMock, patch

import pyiceberg.types as T
import pytest
from ordeq import IOException
from ordeq_iceberg import (
    IcebergCatalog,
    IcebergTable,
    IfTableExistsSaveOptions,
)
from pyiceberg.catalog import CatalogType
from pyiceberg.catalog.memory import InMemoryCatalog
from pyiceberg.schema import NestedField, Schema


@pytest.fixture(scope="module")
def catalog_io() -> IcebergCatalog:
    return IcebergCatalog(
        name="test_catalog", catalog_type=CatalogType.IN_MEMORY
    )


@pytest.fixture(scope="module")
def catalog(catalog_io) -> InMemoryCatalog:
    catalog = cast("InMemoryCatalog", catalog_io.load())
    catalog.create_namespace("test_namespace")
    return catalog


def test_create_table(catalog: InMemoryCatalog):
    table_create = IcebergTable(
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
    table_create = IcebergTable(
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


def test_create_table_with_iceberg_schema(catalog: InMemoryCatalog):
    schema = Schema(
        NestedField(
            field_id=1, name="id", field_type=T.IntegerType(), required=True
        ),
        NestedField(
            field_id=2, name="data", field_type=T.StringType(), required=False
        ),
    )
    table_create = IcebergTable(
        catalog=catalog,
        table_name="test_table_schema",
        namespace="test_namespace",
        schema=schema,
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    table_create.save(None)
    assert catalog.table_exists("test_namespace.test_table_schema")


def test_create_existing_table_raises(catalog: InMemoryCatalog):
    table_create = IcebergTable(
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
        match=r"Table 'test_namespace.test_table_existing' already exists",
    ):
        table_create.save(None)


def test_create_existing_table_ignore(catalog: InMemoryCatalog):
    table_create = IcebergTable(
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


@patch("ordeq_iceberg.table.IcebergTable._catalog_value")
@patch("ordeq_iceberg.table.IcebergTable.table_exists")
def test_create_existing_table_drop(
    mock_table_exists: MagicMock,
    mock_catalog: MagicMock,
    catalog: InMemoryCatalog,
):
    mock_table_exists.return_value = True
    table_create = IcebergTable(
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
    mock_catalog.drop_table.assert_called_once()
    mock_catalog.create_table.assert_called_once()


@patch("ordeq_iceberg.table.IcebergTable._catalog_value")
@patch("ordeq_iceberg.table.IcebergTable.table_exists")
def test_create_existing_table_if_exists_null(
    mock_table_exists: MagicMock, mock_catalog: MagicMock
):
    mock_table_exists.return_value = True
    table_create = IcebergTable(
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


@patch("ordeq_iceberg.table.IcebergTable._catalog_value")
@patch("ordeq_iceberg.table.IcebergTable.table_exists")
def test_if_exists_drop_as_string(
    mock_table_exists: MagicMock,
    mock_catalog: MagicMock,
    catalog: InMemoryCatalog,
):
    mock_table_exists.return_value = True
    table_create = IcebergTable(
        catalog=catalog,
        table_name="test_table_if_exists_str",
        namespace="test_namespace",
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),
        if_exists="drop",
    )
    table_create.save(None)
    mock_catalog.drop_table.assert_called_once()
    mock_catalog.create_table.assert_called_once()
