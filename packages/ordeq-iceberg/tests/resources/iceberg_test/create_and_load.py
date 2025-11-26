import pyiceberg.types as T
from ordeq import node, run
from ordeq_common import Literal
from ordeq_iceberg import (
    IcebergCatalog,
    IcebergTable,
    IfTableExistsSaveOptions,
)
from pyiceberg.catalog import Catalog, CatalogType
from pyiceberg.table import Table

# Catalog

my_catalog = IcebergCatalog(
    name="test_catalog", catalog_type=CatalogType.IN_MEMORY
)

test_namespace = Literal[str]("test_namespace")
test_table_name = "test_table"

table_resource = f"{test_table_name}.{test_namespace.value}"

my_table = IcebergTable(
    catalog=my_catalog,
    table_name=test_table_name,
    namespace=test_namespace.value,
    schema=T.StructType(
        T.NestedField(1, "id", T.IntegerType(), required=True),
        T.NestedField(2, "data", T.StringType(), required=False),
    ),  # Schema is required for saving
    if_exists=IfTableExistsSaveOptions.DROP,
)

# Nodes


@node(inputs=[my_catalog, test_namespace], outputs=[my_table])
def create_save_table(catalog: Catalog, namespace: str) -> None:
    catalog.create_namespace_if_not_exists(namespace)


@node(inputs=[my_table])
def load_table(created_table: Table):
    print(f"Table loaded from Input object: '{created_table}'")


run(create_save_table, load_table)
