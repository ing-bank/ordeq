import pyiceberg.types as T
import pytest
from ordeq_iceberg import IcebergCatalog, IcebergTable
from pyiceberg.catalog.sql import SqlCatalog
from pyiceberg.schema import Schema
from pyiceberg.table import Table


@pytest.fixture(scope="module")
def create_test_table(sql_catalog: SqlCatalog) -> Table:
    schema = Schema(
        *(
            T.StructType(
                T.NestedField(1, "id", T.IntegerType(), required=True),
                T.NestedField(2, "data", T.StringType(), required=False),
            ).fields
        )
    )
    return sql_catalog.create_table(
        identifier="test_namespace.test_table", schema=schema
    )


def test_load_table(sql_catalog: SqlCatalog, create_test_table: Table):
    table = IcebergTable(
        catalog=sql_catalog,
        table_name="test_table",
        namespace="test_namespace",
    )
    assert table.load() == create_test_table


def test_load_table_with_catalog_io(
    sql_catalog_io: IcebergCatalog, create_test_table: Table
):
    table = IcebergTable(
        catalog=sql_catalog_io,
        table_name="test_table",
        namespace="test_namespace",
    )
    assert table.load() == create_test_table
