import os
from dataclasses import KW_ONLY, dataclass

from ordeq.framework.io import IO


@dataclass(frozen=True)
class EnvironmentVariable(IO[str]):
    """IO used to load and save environment variables. Use:
        - as input, to parameterize the node logic
        - as output, to set an environment variable based on node logic

    Gets and sets `os.environ` on load and save. See [1] for more
    information.

    [1] https://docs.python.org/3/library/os.html#os.environ

    Example in a node:

    ```pycon
    >>> from ordeq import node
    >>> from ordeq_spark import SparkHiveTable
    >>> import pyspark.sql.functions as F
    >>> from pyspark.sql import DataFrame

    >>> @node(
    ...    inputs=[
    ...         SparkHiveTable(table="my.table"),
    ...         EnvironmentVariable("KEY", default="DEFAULT")
    ...    ],
    ...    outputs=SparkHiveTable(table="my.output"),
    ... )
    ... def transform(df: DataFrame, value: str) -> DataFrame:
    ...     return df.where(F.col("col") == value)

    ```

    When you run `transform` through the CLI as follows:

    ```shell
    export KEY=MyValue
    python {your-entrypoint} run --node transform
    ```

    `MyValue` will be used as `value` in `transform`.

    """

    key: str
    _: KW_ONLY
    default: str | None = None

    def load(self) -> str:
        if self.default:
            return os.environ.get(self.key, self.default)
        return os.environ[self.key]

    def save(self, value: str) -> None:
        os.environ[self.key] = value
