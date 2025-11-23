from ordeq import node
from pyiceberg.catalog import Catalog
from pyiceberg.table import Table
from resources.iceberg_test.catalog import (
    my_catalog,
    my_table,
    my_table_create,
    test_namespace,
)


@node(inputs=[my_catalog, test_namespace], outputs=[my_table_create])
def create_save_table(catalog: Catalog, namespace: str) -> Catalog:
    catalog.create_namespace(namespace)


@node(inputs=[my_table])
def load_table(created_table: Table):
    print(f"Table loaded from Input object: '{created_table}'")
