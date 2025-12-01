## Resource

```python
import pyiceberg.types as T
from ordeq import node, run
from ordeq_common import Literal
from ordeq_iceberg import IcebergCatalog, IcebergTable
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


@node(inputs=[my_catalog, test_namespace, test_table_name])
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


@node(inputs=[my_table, create_table])
def load_table(created_table: Table, _: None) -> None:
    print(f"Table loaded from Input object: '{created_table}'")


run(load_table)

```

## Output

```text
Table loaded from Input object: 'test_table(
  1: id: required int,
  2: data: optional string
),
partition by: [],
sort order: [],
snapshot: null'

```

## Logging

```text
INFO	ordeq.io	Loading IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>)
DEBUG	ordeq.io	Persisting data for IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>)
INFO	ordeq.io	Loading Literal('test_namespace')
DEBUG	ordeq.io	Persisting data for Literal('test_namespace')
INFO	ordeq.io	Loading Literal('test_table')
DEBUG	ordeq.io	Persisting data for Literal('test_table')
INFO	ordeq.runner	Running view 'create_table' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.io	Loading IcebergTable(catalog=IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>), table_name='test_table', namespace='test_namespace')
DEBUG	ordeq.io	Loading cached data for IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>)
DEBUG	ordeq.io	Persisting data for IcebergTable(catalog=IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>), table_name='test_table', namespace='test_namespace')
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
INFO	ordeq.runner	Running view 'load_table' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>)
DEBUG	ordeq.io	Unpersisting data for Literal('test_namespace')
DEBUG	ordeq.io	Unpersisting data for Literal('test_table')
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IcebergTable(catalog=IcebergCatalog(name='test_catalog', catalog_type=<CatalogType.IN_MEMORY: 'in-memory'>), table_name='test_table', namespace='test_namespace')
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```