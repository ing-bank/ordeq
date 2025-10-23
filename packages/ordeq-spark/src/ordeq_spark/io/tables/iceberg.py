from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, cast

import pyspark.sql.functions as F
from ordeq import IO
from pyspark.sql import Column, DataFrame
from pyspark.sql.utils import CapturedException

if TYPE_CHECKING:
    try:
        from pyspark.sql import (  # type: ignore[attr-defined]
            DataFrameWriterV2 as DataFrameWriter,  # ty: ignore[unresolved-import]
        )
    except ImportError:
        from pyspark.sql import DataFrameWriter  # type: ignore[assignment]

from pyspark.sql.utils import AnalysisException

from ordeq_spark.io.tables.table import SparkTable
from ordeq_spark.utils import apply_schema

SparkIcebergWriteMode = Literal[
    "create", "createOrReplace", "overwrite", "overwritePartitions", "append"
]


@dataclass(frozen=True, kw_only=True)
class SparkIcebergTable(SparkTable, IO[DataFrame]):
    """IO used to load & save Iceberg tables using Spark.

    Example usage:

    ```pycon
    >>> from ordeq_spark import (
    ...     SparkIcebergTable
    ... )
    >>> from pyspark.sql.types import StructType, StructField, IntegerType
    >>> MyTable = SparkIcebergTable(
    ...     table="my.iceberg.table",
    ...     schema=StructType(
    ...         fields=[
    ...             StructField("id", IntegerType()),
    ...             StructField("amount", IntegerType()),
    ...         ]
    ...     )
    ... )

    >>> import pyspark.sql.functions as F
    >>> MyPartitionedTable = (
    ...     SparkIcebergTable(
    ...         table="my.iceberg.table"
    ...     ).with_save_options(
    ...         mode="overwritePartitions",
    ...         partition_by=(
    ...             ("colour",),
    ...             (F.years, "dt"),
    ...         )
    ...     )
    ... )

    ```

    If `schema` is provided, it will be applied before save and after load.

    Saving is idempotent: if the target table does not exist, it is
    created with the configuration set in the save options.

    Table properties can be specified on the `properties` attribute.
    Currently, the properties will be taken into account on write only.

    ```pycon
    >>> TableWithProperties = SparkIcebergTable(
    ...     table="my.iceberg.table",
    ...     properties=(
    ...         ('read.split.target-size', '268435456'),
    ...         ('write.parquet.row-group-size-bytes', '268435456'),
    ...     )
    ... )

    ```

    Currently only supports a subset of Iceberg writes. More info [1]:

    [1]: https://iceberg.apache.org/docs/nightly/spark-writes/

    """

    properties: tuple[tuple[str, str], ...] = ()

    def save(
        self,
        df: DataFrame,
        mode: SparkIcebergWriteMode = "overwritePartitions",
        partition_by: tuple[
            tuple[Callable[[str], Column], str] | tuple[str], ...
        ] = (),
    ) -> None:
        """Saves the DataFrame to the Iceberg table.

        Args:
            df: DataFrame to save
            mode: write mode, one of:
                - "create" - create the table, fail if it exists
                - "createOrReplace" - create the table, replace if it exists
                - "overwrite" - overwrite the table
                - "overwritePartitions" - overwrite partitions of the table
                - "append" - append to the table
            partition_by: tuple of columns to partition by, each element can be
                - a tuple of a function and a column name, e.g. (F.years, "dt")
                - a single column name as a string, e.g. "colour"

        Raises:
            TypeError: if partition_by is not a tuple of tuples
            ValueError: if mode is not one of the supported modes
            RuntimeError: if the Spark captured exception cannot be parsed
            CapturedException: if there is an error during the write operation
        """
        df = apply_schema(df, self.schema) if self.schema else df
        if partition_by:
            partition_cols = []
            for t in partition_by:
                if not isinstance(t, tuple):
                    raise TypeError(
                        f"Expected partition_by to be a tuple of tuples, "
                        f"got {type(t)}: {t}"
                    )
                if len(t) == 2 and callable(t[0]):
                    partition_cols.append(t[1])  # type: ignore[index-out-of-bounds]
                elif len(t) == 1 and isinstance(t[0], str):
                    # Otherwise, we assume it is a single column name
                    partition_cols.append(t[0])  # type: ignore[index-out-of-bounds]
                else:
                    raise TypeError(
                        f"Expected partition_by to be a tuple of tuples with "
                        f"either 1 or 2 elements, got {len(t)}: {t}"
                    )
            df = df.sortWithinPartitions(*partition_cols)
        writer = self._writer(df, partition_by)
        try:
            match mode:
                case "overwrite":
                    # Full overwrite
                    return writer.overwrite(F.lit(True))
                case "overwritePartitions":
                    return writer.overwritePartitions()
                case "append":
                    return writer.append()
                case "create" | "createOrReplace":
                    return writer.createOrReplace()
                case _:
                    raise ValueError(f"Unexpected write mode {mode}")
        # pyspark errors are captured here as CapturedException. A
        # better, more granular exception seems
        # 'pyspark.errors.AnalysisException', but it is only available in more
        # recent versions of PySpark
        except CapturedException as exc:
            # compatibility spark 3 and 4
            if hasattr(exc, "desc"):
                desc = cast("str", exc.desc)
            elif hasattr(exc, "_desc"):
                desc = cast("str", exc._desc)  # noqa: SLF001
            else:
                raise RuntimeError(
                    "Expecting CapturedException to have a `desc` or `_desc` "
                    "attribute."
                ) from exc
            if exc.getErrorClass() == "TABLE_OR_VIEW_NOT_FOUND" or (
                "UnresolvedRelation" in desc
                and isinstance(exc, AnalysisException)
            ):
                return writer.createOrReplace()
            raise

    def _writer(
        self,
        df: DataFrame,
        partition_by: tuple[
            tuple[Callable[[str], Column], str] | tuple[str], ...
        ],
    ) -> "DataFrameWriter":
        """Returns a Spark DataFrame writer configured by save options.

        Args:
            df: DataFrame
            partition_by: tuple of columns to partition by

        Returns:
            the writer

        Raises:
            TypeError: if partition_by is not a tuple of tuples
        """

        writer = df.writeTo(self.table).using("iceberg")
        for k, v in self.properties:
            writer = writer.tableProperty(k, v)
        if partition_by:
            partitions = []
            for t in partition_by:
                if not isinstance(t, tuple):
                    raise TypeError(
                        f"Expected partition_by to be a tuple of tuples, "
                        f"got {type(t)}: {t}"
                    )
                if len(t) == 2 and callable(t[0]):
                    partitions.append(t[0](t[1]))  # type: ignore[index-out-of-bounds]
                elif len(t) == 1 and isinstance(t[0], str):
                    # Otherwise, we assume it is a single column name
                    partitions.append(F.col(t[0]))
                else:
                    raise TypeError(
                        f"Expected partition_by to be a tuple of tuples with "
                        f"either 1 or 2 elements, got {len(t)}: {t}"
                    )

            writer.partitionedBy(*partitions)
        return writer
