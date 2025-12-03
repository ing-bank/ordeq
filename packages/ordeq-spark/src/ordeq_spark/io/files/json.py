from dataclasses import dataclass
from typing import Any

from ordeq import IO
from pyspark.sql import DataFrame, SparkSession


@dataclass(frozen=True, kw_only=True)
class SparkJSON(IO[DataFrame]):
    """IO for loading and saving JSON using Spark.

    Example:

    ```pycon
    >>> from ordeq_spark import SparkJSON
    >>> json = SparkJSON(
    ...     path="to.json"
    ... )

    ```
    """

    path: str
    format: str = "json"

    def load(self, **load_options: Any) -> DataFrame:
        """
        Load a JSON into a DataFrame.

        Args:
            load_options: Additional options for loading.

        Returns:
            The loaded DataFrame.
        """
        return SparkSession.builder.getOrCreate().read.load(
            path=self.path, format=self.format, **load_options
        )

    def save(self, df: DataFrame, **save_options: Any) -> None:
        """
        Save a DataFrame to JSON.

        Args:
            df: The DataFrame to save.
            save_options: Additional options for saving.
        """
        df.write.save(path=self.path, format=self.format, **save_options)
