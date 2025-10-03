from dataclasses import dataclass
from typing import Literal

from ordeq import IO
from pyspark.sql import DataFrame

from ordeq_spark.utils import get_spark_session


@dataclass(frozen=True, kw_only=True)
class SparkGlobalTempView(IO[DataFrame]):
    """IO for reading from and writing to Spark global temporary views.

    Examples:

    Create and save a DataFrame to a global temp view:

    ```pycon
    >>> from ordeq_spark import SparkGlobalTempView
    >>> from pyspark.sql import SparkSession
    >>> spark = SparkSession.builder.getOrCreate()  # doctest: +SKIP
    >>> view = SparkGlobalTempView(table="my_temp_view")
    >>> df = spark.createDataFrame(
    ...     [(1, "Alice"), (2, "Bob")], ["id", "name"]
    ... )  # doctest: +SKIP
    >>> view.save(df, mode="createOrReplace")  # doctest: +SKIP

    ```

    Load the DataFrame from the global temp view:

    ```pycon
    >>> loaded_df = view.load()  # doctest: +SKIP
    >>> loaded_df.show()  # doctest: +SKIP

    ```

    """

    table: str

    def load(self) -> DataFrame:
        return get_spark_session().table(f"global_temp.{self.table}")

    def save(
        self,
        df: DataFrame,
        mode: Literal["create", "createOrReplace"] = "create",
    ) -> None:
        if mode == "create":
            df.createGlobalTempView(self.table)
        if mode == "createOrReplace":
            df.createOrReplaceGlobalTempView(self.table)
