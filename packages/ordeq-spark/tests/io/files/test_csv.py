from pathlib import Path

from ordeq_spark import SparkCSV
from pyspark.sql import SparkSession


def test_it_saves_and_loads(spark: SparkSession, tmpdir):
    csv_path = str(tmpdir / "test.csv")
    cols = ["id", "colour"]
    df = spark.createDataFrame([(1, "yellow"), (2, "orange")], schema=cols)

    csv_file = SparkCSV(path=csv_path)
    csv_file.save(df, header=True)
    assert Path(csv_path).is_dir()
    assert len(list(Path(csv_path).glob("*.csv"))) > 0

    loaded = csv_file.load(header=True)
    loaded_rows = [tuple(row) for row in loaded.collect()]
    assert set(loaded_rows) == {("1", "yellow"), ("2", "orange")}
