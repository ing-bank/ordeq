from dataclasses import dataclass

import pyspark.sql
from ordeq import Input

from ordeq_spark.utils import get_spark_session


@dataclass(frozen=True)
class SparkSession(Input[pyspark.sql.SparkSession]):
    """Input representing the active Spark session. Useful for accessing the
    active Spark session in nodes.

    Example:

    ```pycon
    >>> from ordeq_spark.io.session import SparkSession
    >>> spark_session = SparkSession()
    >>> spark = spark_session.load()  # doctest: +SKIP
    >>> print(spark.version)  # doctest: +SKIP
    3.3.1

    ```

    Example in a node:

    ```pycon
    >>> from ordeq import node, Input
    >>> items = Input[dict]({'id': [1, 2, 3], 'value': ['a', 'b', 'c']})
    >>> @node(
    ...     inputs=[items, spark_session],
    ...     outputs=[],
    ... )
    ... def convert_to_df(
    ...     data: dict, spark: pyspark.sql.SparkSession
    ... ) -> pyspark.sql.DataFrame:
    ...     return spark.createDataFrame(data)

    ```

    """

    def load(self) -> pyspark.sql.SparkSession:
        """Gets the active SparkSession. Errors if there is no active
        Spark session.

        Returns:
            pyspark.sql.SparkSession: The Spark session.

        """

        return get_spark_session()
