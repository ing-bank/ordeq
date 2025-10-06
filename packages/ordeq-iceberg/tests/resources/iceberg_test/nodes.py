from resources.iceberg_test.catalog import my_catalog, my_save_table, test_namespace
from ordeq import node
from pyiceberg.catalog import Catalog
from pyiceberg.table import Table

@node(inputs=[my_catalog, test_namespace], outputs=[my_save_table])
def create_save_table(catalog: Catalog, namespace: str) -> Catalog:
    catalog.create_namespace(namespace)

@node(inputs=[my_catalog, my_save_table], outputs=[])
def load_table(catalog: Catalog, save_table: Table) -> None:
    loaded_table = catalog.load_table("test_namespace.new_test_table")
    print(f"Table loaded from catalog: '{loaded_table}'")
    print(f"Table loaded from IO object: '{save_table}'")
