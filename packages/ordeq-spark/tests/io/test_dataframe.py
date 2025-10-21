from ordeq_spark import SparkDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    IntegerType,
    Row,
    StringType,
    StructField,
    StructType,
)


def test_it_loads(spark: SparkSession):
    assert SparkDataFrame(
        schema=StructType(
            fields=[
                StructField("village", StringType()),
                StructField("hobbit_count", IntegerType()),
            ]
        ),
        data=(("Appleford", 6), ("Brothbridge", 19), ("Cheeseshire", 14)),
    ).load().collect() == [
        Row(village="Appleford", hobbit_count=6),
        Row(village="Brothbridge", hobbit_count=19),
        Row(village="Cheeseshire", hobbit_count=14),
    ]
