from dataclasses import dataclass
from typing import Literal

from ordeq import IO
from pyspark.sql import DataFrame

from ordeq_spark.io.tables.table import SparkTable
from ordeq_spark.io.types import SparkFormat
from ordeq_spark.utils import apply_schema

SparkWriteMode = Literal["overwrite", "append", "errorifexists", "ignore"]


@dataclass(frozen=True, kw_only=True)
class SparkHiveTable(SparkTable, IO[DataFrame]):
    """IO for reading from and writing to Hive tables in Spark.

    Examples:

    Save a DataFrame to a Hive table:

    ```pycon
    >>> from ordeq_spark import SparkHiveTable
    >>> from pyspark.sql import SparkSession
    >>> spark = SparkSession.builder.enableHiveSupport().getOrCreate()  # doctest: +SKIP
    >>> table = SparkHiveTable(table="my_hive_table")
    >>> df = spark.createDataFrame(
    ...     [(1, "Alice"), (2, "Bob")], ["id", "name"]
    ... )  # doctest: +SKIP
    >>> table.save(df, format="parquet", mode="overwrite")  # doctest: +SKIP

    ```

    If `schema` is provided, it will be applied before save and after load.

    """  # noqa: E501 (line too long)

    def save(
        self,
        df: DataFrame,
        format: SparkFormat = "parquet",  # noqa: A002
        mode: SparkWriteMode = "overwrite",
        partition_by: str | list[str] | None = None,
    ) -> None:
        df = apply_schema(df, self.schema) if self.schema else df
        df.write.saveAsTable(
            name=self.table, format=format, mode=mode, partitionBy=partition_by
        )
