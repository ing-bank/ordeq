import polars as pl
from ordeq_polars import PolarsEagerIceberg, PolarsLazyIceberg


def test_it_saves_append(iceberg_table: str, df: pl.DataFrame):
    iceberg = PolarsEagerIceberg(path=iceberg_table)

    # Save initial data
    iceberg.save(df, mode="overwrite")

    # Save more data
    iceberg.save(df, mode="append")

    # Should have double the rows
    result = PolarsLazyIceberg(path=iceberg.path).load().collect()
    expected = pl.concat([df, df])
    assert result.equals(expected)
