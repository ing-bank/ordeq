import polars as pl
from ordeq_polars import PolarsLazyIceberg
from pyiceberg.table import Table


def test_it_loads(iceberg_table: Table, lf: pl.LazyFrame):
    # First create an Iceberg table
    lf.collect().write_iceberg(target=iceberg_table, mode="overwrite")

    # Then test loading from it
    result = PolarsLazyIceberg(path=iceberg_table).load()
    assert result.collect().equals(lf.collect())
