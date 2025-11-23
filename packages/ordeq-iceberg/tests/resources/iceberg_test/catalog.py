import pyiceberg.types as T
from ordeq_common import Literal
from pyiceberg.catalog import CatalogType

from ordeq_iceberg import (
    IcebergCatalog,
    IcebergTable,
    IcebergTableCreate,
    IfTableExistsSaveOptions,
)

my_catalog = IcebergCatalog(name="test_catalog", catalog_type=CatalogType.IN_MEMORY)

test_namespace = Literal[str]("test_namespace")
test_table_name = "test_table"

table_resource = f"{test_table_name}.{test_namespace.value}"

my_table = (
    IcebergTable(
        catalog=my_catalog, table_name=test_table_name, namespace=test_namespace.value
    )
    @ table_resource
)

my_table_create = (
    IcebergTableCreate(
        catalog=my_catalog,
        table_name=test_table_name,
        namespace=test_namespace.value,
        schema=T.StructType(
            T.NestedField(1, "id", T.IntegerType(), required=True),
            T.NestedField(2, "data", T.StringType(), required=False),
        ),  # Schema is required for saving
        if_exists=IfTableExistsSaveOptions.DROP,
    )
    @ table_resource
)
