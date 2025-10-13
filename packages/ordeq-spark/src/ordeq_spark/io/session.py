from dataclasses import dataclass

import pyspark.sql
from ordeq import Input


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
    >>> from ordeq import node
    >>> from ordeq_common import Literal
    >>> items = Literal({'id': [1, 2, 3], 'value': ['a', 'b', 'c']})
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
        """Gets the active SparkSession

        Returns:
            pyspark.sql.SparkSession: The Spark session.

        Raises:
            ValueError: If there is no active Spark session.
        """

        session = pyspark.sql.SparkSession.getActiveSession()
        if session is None:
            raise ValueError("Spark session must be active")
        return session
