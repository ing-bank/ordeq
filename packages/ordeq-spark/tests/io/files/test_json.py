import json
from pathlib import Path

from ordeq_spark import SparkJSON
from pyspark.sql import SparkSession


def test_it_loads(spark: SparkSession, tmpdir):
    data = {"foo": "bar", "baz": 42}
    json_path = tmpdir / "test.json"
    json_path.write(json.dumps(data))

    json_file = SparkJSON(path=str(json_path))
    loaded = json_file.load()
    loaded_dict = loaded.collect()[0].asDict()
    assert loaded_dict == data


def test_it_saves(spark: SparkSession, tmpdir):
    json_path = tmpdir / "test.json"
    json_file = SparkJSON(path=str(json_path))
    cols = ["id", "colour"]
    df = spark.createDataFrame([(1, "yellow"), (2, "orange")], schema=cols)

    json_file.save(df)

    assert Path(json_path).is_dir()
