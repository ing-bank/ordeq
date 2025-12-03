from dataclasses import dataclass
from typing import Any

from ordeq import IO
from pyspark.sql import DataFrame, SparkSession


@dataclass(frozen=True, kw_only=True)
class SparkCSV(IO[DataFrame]):
    """IO for loading and saving CSV using Spark.

    Example:

    ```pycon
    >>> from ordeq_spark import SparkCSV
    >>> csv = SparkCSV(
    ...     path="to.csv"
    ... ).with_load_options(
    ...     infer_schema=True
    ... )

    ```
    """

    path: str
    format: str = "csv"

    def load(
        self,
        infer_schema: bool = True,
        header: bool = True,
        **load_options: Any,
    ) -> DataFrame:
        """
        Load a CSV into a DataFrame.

        Args:
            infer_schema: Whether to infer the schema.
            header: Whether the CSV has a header row.
            load_options: Additional options for loading.

        Returns:
            The loaded DataFrame.
        """
        return SparkSession.builder.getOrCreate().read.load(
            path=self.path,
            format=self.format,
            infer_schema=infer_schema,
            header=header,
            **load_options,
        )

    def save(self, df: DataFrame, **save_options: Any) -> None:
        """
        Save a DataFrame to CSV.

        Args:
            df: The DataFrame to save.
            save_options: Additional options for saving.
        """
        df.write.save(path=self.path, format=self.format, **save_options)
