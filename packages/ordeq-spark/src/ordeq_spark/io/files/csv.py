from dataclasses import dataclass

from ordeq import IO
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType

from ordeq_spark.io.files.utils import _save_single_file
from ordeq_spark.utils import apply_schema


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

    By default, Spark creates a directory on save.
    Use `single_file` if you want to write to a file instead:

    ```pycon
    >>> from ordeq_spark import SparkCSV
    >>> csv = SparkCSV(
    ...     path="to.json"
    ... ).with_load_options(single_file=True)

    ```

    """

    path: str
    format: str = "csv"
    schema: StructType | None = None

    def load(
        self, infer_schema: bool = True, header: bool = True, **load_options
    ) -> DataFrame:
        df = SparkSession.builder.getOrCreate().read.load(
            path=self.path,
            format=self.format,
            infer_schema=infer_schema,
            header=header,
            **load_options,
        )
        return apply_schema(df, self.schema) if self.schema else df

    def save(
        self, df: DataFrame, single_file: bool = False, **save_options
    ) -> None:
        df = apply_schema(df, self.schema) if self.schema else df
        if single_file:
            _save_single_file(df, self.path, self.format, **save_options)
        else:
            df.write.save(path=self.path, format=self.format, **save_options)
