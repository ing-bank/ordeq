from ordeq_iceberg.catalog import IcebergInMemoryCatalog
from ordeq_iceberg.table import IcebergTable, IcebergTableCreate
import pyiceberg.types as T
from ordeq_common import Literal

my_catalog = IcebergInMemoryCatalog(name="test_catalog")

test_namespace = Literal[str]("test_namespace")

my_load_table = IcebergTable(
    catalog=my_catalog,
    table_name="new_test_table",
    namespace=test_namespace.value,
)

my_save_table = IcebergTableCreate(
    table=my_load_table,
    schema=T.StructType(
        T.NestedField(1, "id", T.IntegerType(), required=True),
        T.NestedField(2, "data", T.StringType(), required=False),
    ),
)
