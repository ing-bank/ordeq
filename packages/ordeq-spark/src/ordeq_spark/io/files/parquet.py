from dataclasses import dataclass
from typing import Any

from ordeq import IO
from pyspark.sql import DataFrame, SparkSession


@dataclass(frozen=True, kw_only=True)
class SparkParquet(IO[DataFrame]):
    """IO for loading and saving Parquet files using Spark.

    Basic usage:

    ```pycon
    >>> from ordeq_spark import SparkParquet
    >>> parquet = SparkParquet(path="data.parquet")
    >>> df = parquet.load()  # doctest: +SKIP
    >>> parquet.save(df)  # doctest: +SKIP
    ```

    Loading with options:

    ```pycon
    >>> df = parquet.load(
    ...     modifiedBefore="2050-07-01T08:30:00"
    ... )  # doctest: +SKIP
    ```

    Saving with options:

    ```pycon
    >>> parquet.save(
    ...     df,
    ...     mode="overwrite",
    ...     compression="brotli"
    ... ) # doctest: +SKIP
    ```

    """

    path: str

    def load(self, **load_options: Any) -> DataFrame:
        """
        Loads a Parquet file into a Spark DataFrame.

        Args:
            load_options: Additional options to pass to Spark's read.parquet
                method.

        Returns:
            A Spark DataFrame containing the data from the Parquet file.
        """
        return SparkSession.builder.getOrCreate().read.parquet(
            self.path, **load_options
        )

    def save(self, df: DataFrame, **save_options: Any) -> None:
        """
        Saves a Spark DataFrame to a Parquet file.

        Args:
            df: The Spark DataFrame to save.
            save_options: Additional options to pass to Spark's write.parquet
                method.
        """
        df.write.parquet(path=self.path, **save_options)
