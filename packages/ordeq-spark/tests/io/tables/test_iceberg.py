from datetime import date

import pyspark.sql.functions as F
import pytest
from ordeq_spark import SparkIcebergTable
from pyspark.sql import SparkSession


# noinspection SqlNoDataSourceInspection
def test_it_saves_by_overwriting(spark: SparkSession):
    table = "TestSparkIcebergTable_test_it_saves_by_overwriting"
    cols = ["id", "colour"]
    df = spark.createDataFrame([(1, "yellow")], schema=cols)
    SparkIcebergTable(table=table).save(df)
    actual = spark.sql(f"SELECT {','.join(cols)} FROM {table}")
    assert set(actual.collect()) == set(df.collect())


@pytest.mark.parametrize(
    "mode",
    [
        "create",
        "createOrReplace",
        "overwrite",
        "append",
        "overwritePartitions",
    ],
)
def test_it_saves_if_not_exists(spark: SparkSession, mode: str):
    table = f"default.TestSparkIcebergTable_test_it_saves_if_not_exists_{mode}"
    cols = ["id", "colour", "abbr"]
    expected = spark.createDataFrame(
        [(1, "yellow", "y"), (2, "green", "g")], schema=cols
    )
    SparkIcebergTable(table=table).save(expected, mode=mode)
    actual = spark.table(table)
    assert actual.sort(cols).collect() == expected.sort(cols).collect()


@pytest.mark.parametrize(
    ("mode", "update_data", "expected_data"),
    [
        ("create", [(2, "green", "g")], [(2, "green", "g")]),
        ("createOrReplace", [(2, "green", "g")], [(2, "green", "g")]),
        (
            "overwrite",
            [
                (1, "YELLOW", "Y"),  # updated record
                (2, "green", "gr"),
            ],
            [
                (1, "YELLOW", "Y"),  # updated record
                (2, "green", "gr"),  # unchanged record
            ],
        ),
        (
            "append",
            [(3, "blue", "b")],
            [(1, "yellow", "y"), (2, "green", "g"), (3, "blue", "b")],
        ),
        (
            "overwritePartitions",
            [
                (2, "GREEN", "GR"),  # updated record
                (3, "blue", "b"),  # new record
            ],
            [
                (1, "yellow", "y"),  # unchanged record
                (2, "GREEN", "GR"),  # updated record
                (3, "blue", "b"),  # new record
            ],
        ),
    ],
)
def test_it_saves_if_exists(
    spark: SparkSession, mode: str, update_data, expected_data
):
    table = f"default.TestSparkIcebergTable_test_it_saves_if_exists_{mode}"
    cols = ["id", "colour", "abbr"]

    # Creates the table and initialize with some seed data.
    # The table is partitioned by 'id'.
    SparkIcebergTable(table=table).with_save_options(
        mode="create", partition_by=((F.col, "id"),)
    ).save(
        spark.createDataFrame(
            [(1, "yellow", "y"), (2, "green", "g")], schema=cols
        )
    )

    # Save the actual data:
    SparkIcebergTable(table=table).save(
        spark.createDataFrame(update_data, schema=cols),
        mode=mode,
        partition_by="id",
    )
    actual = spark.table(table)
    expected = spark.createDataFrame(expected_data, schema=cols)
    assert actual.sort(cols).collect() == expected.sort(cols).collect()


def test_it_saves_partitioned_by_transformed_column(spark: SparkSession):
    iceberg = SparkIcebergTable(
        table="test_it_saves_partitioned_by_transformed_column"
    ).with_save_options(
        mode="overwritePartitions", partition_by=((F.years, "dt"),)
    )
    cols = ["dt", "val"]
    iceberg.save(
        spark.createDataFrame(
            [(date(2021, 12, 31), "A"), (date(2023, 4, 12), "B")], schema=cols
        )
    )
    iceberg.save(
        spark.createDataFrame(
            [(date(2021, 11, 4), "F"), (date(2024, 4, 12), "C")], schema=cols
        )
    )
    expected = spark.createDataFrame(
        [
            (date(2021, 11, 4), "F"),  # got updated
            (date(2023, 4, 12), "B"),  # unchanged
            (date(2024, 4, 12), "C"),  # got added
        ],
        schema=cols,
    )
    assert (
        spark.table(iceberg.table).sort(cols).collect()
        == expected.sort(cols).collect()
    )


def test_it_saves_with_table_properties(spark: SparkSession):
    table = "test_it_saves_with_table_properties"
    properties = (
        ("read.split.target-size", "268435456"),
        ("write.parquet.row-group-size-bytes", "268435456"),
        ("history.expire.min-snapshots-to-keep", "0"),
        ("commit.retry.num-retries", "8"),
    )
    iceberg = SparkIcebergTable(table=table, properties=properties)
    iceberg.save(
        spark.createDataFrame(
            [("A", "Amsterdam"), ("B", "Bilbao")], schema=["key", "val"]
        )
    )
    description = spark.sql(f"DESCRIBE EXTENDED {table}")
    # DESCRIBE EXTENDED queries table metadata. The result DataFrame
    # looks roughly as follows:
    # +--------------------+--------------------+-------+
    # |            col_name|           data_type|comment|
    # +--------------------+--------------------+-------+
    #  ...
    # |               Owner|              sw05nn|       |
    # |    Table Properties|[commit.retry.num...|       |
    # +--------------------+--------------------+-------+
    # We are only interested in the last row for this test:
    actual = description.where(
        F.col("col_name") == "Table Properties"
    ).collect()
    assert len(actual) == 1
    actual_properties = actual[0]["data_type"]
    # str that looks like '[key1=value1,key2=value2,...]'
    assert all(f"{k}={v}" in actual_properties for k, v in properties)
