from pathlib import Path

from ordeq_spark import SparkParquet
from pyspark.sql import SparkSession


def test_it_loads(spark: SparkSession, tmp_path: Path):
    path = str(tmp_path)
    cols = ["id", "colour"]
    expected = spark.createDataFrame(
        [(1, "yellow"), (2, "orange")], schema=cols
    )
    expected.write.parquet(path, mode="overwrite")
    parquet = SparkParquet(path=path)
    actual = parquet.load()
    assert set(actual.collect()) == set(expected.collect())


def test_it_saves(spark: SparkSession, tmp_path: Path):
    path = str(tmp_path / "data.parquet")
    cols = ["id", "colour"]
    actual = spark.createDataFrame([(1, "yellow"), (2, "orange")], schema=cols)
    parquet = SparkParquet(path=path)
    parquet.save(actual)
    expected = spark.read.parquet(path)
    assert set(actual.collect()) == set(expected.collect())
