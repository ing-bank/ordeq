from dataclasses import dataclass

from ordeq import IO, Input
from pyspark.sql import DataFrame, DataFrameReader, DataFrameWriter
from pyspark.sql.types import StructType

from ordeq_spark.utils import apply_schema, get_spark_session


@dataclass(frozen=True, kw_only=True)
class SparkJDBC:
    """IO for loading from and saving to a database with Spark and JDBC.

    The JDBC driver need to be added to your Spark application. For
    instance, to connect to Microsoft SQL Server, pass
    `com.microsoft.sqlserver:mssql-jdbc:12.8.1.jre11` as extra JAR.

    When saving, the types of the DataFrame should be compatible with the
    target table. More info [1].

    [1] https://spark.apache.org/docs/4.0.0-preview1/sql-data-sources-jdbc.html

    Example:

    ```pycon
    >>> from ordeq_spark import SparkJDBCTable
    >>> SparkJDBCTable(
    ...     table="schema.table",
    ...     driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    ...     url=(
    ...         "jdbc:sqlserver://host:52840"
    ...         "databaseName=tempdb;"
    ...         "user=SA;"
    ...         "password=1Secure*Password1;"
    ...     )
    ...  ).load()  # doctest: +SKIP

    ```

    Use `SparkJDBCQuery` to execute a custom query on load:

    ```pycon
    >>> from ordeq_spark import SparkJDBCQuery
    >>> SparkJDBCQuery(
    ...     query="SELECT 1;",
    ...     driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    ...     url=(
    ...         "jdbc:sqlserver://host:52840"
    ...         "databaseName=tempdb;"
    ...         "user=SA;"
    ...         "password=1Secure*Password1;"
    ...     )
    ...  ).load()  # doctest: +SKIP

    ```
    """

    url: str
    driver: str
    schema: StructType | None = None

    def _reader(self, **kwargs) -> DataFrameReader:
        return (
            get_spark_session()
            .read.format("jdbc")
            .options(url=self.url, driver=self.driver, **kwargs)
        )

    def _writer(self, df: DataFrame, **kwargs) -> DataFrameWriter:
        return df.write.format("jdbc").options(
            url=self.url, driver=self.driver, **kwargs
        )


@dataclass(frozen=True, kw_only=True)
class SparkJDBCTable(IO[DataFrame], SparkJDBC):
    table: str

    def load(self, **load_options) -> DataFrame:
        df = self._reader(dbtable=self.table, **load_options).load()
        return apply_schema(df, self.schema) if self.schema else df

    def save(
        self, df: DataFrame, mode: str = "overwrite", **save_options
    ) -> None:
        df = apply_schema(df, self.schema) if self.schema else df
        self._writer(df, dbtable=self.table, **save_options).save(mode=mode)


@dataclass(frozen=True, kw_only=True)
class SparkJDBCQuery(Input[DataFrame], SparkJDBC):
    query: str

    def load(self) -> DataFrame:
        df = self._reader(query=self.query).load()
        return apply_schema(df, self.schema) if self.schema else df
