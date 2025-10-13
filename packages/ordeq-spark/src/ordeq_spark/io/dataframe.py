from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from ordeq import Input
from pyspark.sql import DataFrame
from pyspark.sql.types import StructType

from ordeq_spark.utils import get_spark_session


@dataclass(frozen=True, kw_only=True, eq=False)
class SparkDataFrame(Input[DataFrame]):
    """Allows a Spark DataFrame to be hard-coded in python. This is suitable
    for small tables such as very simple dimension tables that are unlikely to
    change. It may also be useful in unit testing.

    Example usage:

    ```pycon
    >>> from pyspark.sql.types import *
    >>> from ordeq_spark import SparkDataFrame
    >>> df = SparkDataFrame(
    ...     schema=StructType([
    ...         StructField("year", IntegerType()),
    ...         StructField("datafile", StringType()),
    ...     ]),
    ...     data=(
    ...         (2022, "file_2022.xlsx"),
    ...         (2023, "file_2023.xlsx"),
    ...         (2024, "file_2023.xlsx"),
    ...     )
    ... )

    ```

    """

    data: Iterable[tuple[Any, ...]]
    schema: StructType | None = None

    def load(self) -> DataFrame:
        return get_spark_session().createDataFrame(
            data=self.data,
            schema=self.schema,  # type: ignore[arg-type]
        )
