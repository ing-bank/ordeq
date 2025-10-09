import pytest
from ordeq import IOException
from ordeq_spark import SparkTempView
from pyspark.sql import SparkSession


# noinspection SqlNoDataSourceInspection
def test_it_saves(spark: SparkSession):
    table = "TestHiveTable_test_it_saves"
    view = SparkTempView(table=table)
    cols = ["id", "colour"]
    first_df = spark.createDataFrame([(1, "green"), (2, "red")], schema=cols)
    second_df = spark.createDataFrame(
        [(1, "yellow"), (2, "orange")], schema=cols
    )

    view.save(first_df)

    with pytest.raises(
        IOException,
        match=f"Temporary view '{table}' already exists|"
        f"Cannot create the temporary view `{table}` "
        "because it already exists",
    ):
        view.save(first_df, mode="create")

    view.save(second_df, mode="createOrReplace")

    actual = view.load().select(cols)
    assert set(actual.collect()) == set(second_df.collect())
