from dataclasses import dataclass

from ordeq import IO
from pyspark.sql import DataFrame, SparkSession

from ordeq_spark.io.files.utils import _save_single_file


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

    By default, Spark creates a directory on save.
    Use `single_file` if you want to write to a file instead:

    ```pycon
    >>> from ordeq_spark import SparkJSON
    >>> json = SparkJSON(
    ...     path="to.json"
    ... ).with_save_options(single_file=True)

    ```

    """

    path: str
    format: str = "json"

    def load(self, **load_options) -> DataFrame:
        return SparkSession.builder.getOrCreate().read.load(
            path=self.path, format=self.format, **load_options
        )

    def save(
        self, df: DataFrame, single_file: bool = False, **save_options
    ) -> None:
        if single_file:
            _save_single_file(df, self.path, self.format, **save_options)
        else:
            df.write.save(path=self.path, format=self.format, **save_options)
