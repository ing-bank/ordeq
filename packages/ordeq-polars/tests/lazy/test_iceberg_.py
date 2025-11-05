from pathlib import Path

import polars as pl
import pytest
from ordeq_polars import PolarsLazyIceberg
from pyiceberg.catalog import Catalog, load_catalog
from pyiceberg.schema import Schema
from pyiceberg.table import Table
from pyiceberg.types import LongType, NestedField, StringType


@pytest.fixture
def iceberg_catalog(tmp_path: Path) -> Catalog:
    warehouse_path = tmp_path / "warehouse"
    warehouse_path.mkdir()

    return load_catalog(
        "default", type="in-memory", warehouse=str(warehouse_path)
    )


@pytest.fixture
def iceberg_table(iceberg_catalog: Catalog) -> Table:
    schema = Schema(
        NestedField(
            field_id=1, name="key", field_type=LongType(), required=False
        ),
        NestedField(
            field_id=2, name="value", field_type=StringType(), required=False
        ),
    )
    iceberg_catalog.create_namespace("test")
    iceberg_catalog.create_table("test.sample", schema=schema)
    return iceberg_catalog.load_table("test.sample")


def test_it_loads(iceberg_table: str, lf: pl.LazyFrame):
    # First create an Iceberg table
    lf.collect().write_iceberg(target=iceberg_table, mode="overwrite")

    # Then test loading from it
    result = PolarsLazyIceberg(path=iceberg_table).load()
    assert result.collect().equals(lf.collect())


def test_it_saves_append(iceberg_table: str, lf: pl.LazyFrame):
    iceberg = PolarsLazyIceberg(path=iceberg_table)

    # Save initial data
    iceberg.save(lf, mode="overwrite")

    # Save more data
    iceberg.save(lf, mode="append")

    # Should have double the rows
    result = iceberg.load().collect()
    expected = pl.concat([lf.collect(), lf.collect()])
    assert result.equals(expected)
