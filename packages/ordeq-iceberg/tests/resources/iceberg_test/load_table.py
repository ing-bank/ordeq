import pyiceberg.types as T
from ordeq import node, run
from ordeq_common import Literal
from ordeq_iceberg import IcebergCatalog, IcebergTable
from ordeq_viz import viz
from pyiceberg.catalog import Catalog, CatalogType
from pyiceberg.schema import Schema
from pyiceberg.table import Table

# Catalog

my_catalog = IcebergCatalog(
    name="test_catalog", catalog_type=CatalogType.IN_MEMORY
)

test_namespace = Literal[str]("test_namespace")
test_table_name = Literal[str]("test_table")

my_table = IcebergTable(
    catalog=my_catalog,
    table_name=test_table_name.value,
    namespace=test_namespace.value,
)

# Nodes


@node(inputs=[my_catalog, test_namespace, test_table_name], checks=[my_table])
def create_table(catalog: Catalog, namespace: str, table_name: str) -> None:
    catalog.create_namespace_if_not_exists(namespace)
    catalog.create_table_if_not_exists(
        (namespace, table_name),
        schema=Schema(
            *T.StructType(
                T.NestedField(1, "id", T.IntegerType(), required=True),
                T.NestedField(2, "data", T.StringType(), required=False),
            ).fields
        ),
    )


@node(inputs=[my_table])
def load_table(created_table: Table) -> None:
    print(f"Table loaded from Input object: '{created_table}'")


print(f"Viz Diagram:\n```\n{viz(__name__, fmt='mermaid-md')}\n```")
run(load_table, create_table)
