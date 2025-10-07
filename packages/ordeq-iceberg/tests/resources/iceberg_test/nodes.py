from resources.iceberg_test.catalog import my_catalog, my_load_table, test_namespace, my_save_table
from ordeq import node
from ordeq_common import StringBuffer

from pyiceberg.catalog import Catalog
from pyiceberg.table import Table


 # Technically not required but needed to create dependencies between the node that saves the table and the node that loads it.
saved_namespace = StringBuffer()

@node(inputs=[my_catalog, test_namespace], outputs=[my_save_table, saved_namespace])
def create_save_table(catalog: Catalog, namespace: str) -> tuple[None, str]:
    catalog.create_namespace(namespace)
    return None, namespace

@node(inputs=[my_catalog, saved_namespace, my_load_table], outputs=[])
def load_table(catalog: Catalog, namespace: str, load_table: Table) -> None:
    loaded_table = catalog.load_table(f"{namespace}.new_test_table")
    print(f"Table loaded from catalog: '{loaded_table}'")
    print(f"Load Table loaded from IO object: '{load_table}'")
