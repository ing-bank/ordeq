from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, TypeAlias, cast

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

SparkIcebergWriteMode: TypeAlias = Literal[
    "create", "createOrReplace", "overwrite", "overwritePartitions", "append"
]
SparkIcebergPartitionType: TypeAlias = (
    str
    | Sequence[str]
    | tuple[tuple[Callable[[str], Column], str] | tuple[str], ...]
)


@dataclass(frozen=True, kw_only=True)
class SparkIcebergTable(SparkTable, IO[DataFrame]):
    """IO used to load & save Iceberg tables using Spark.

    Example usage:

    ```pycon
    >>> from ordeq_spark import (
    ...     SparkIcebergTable
    ... )
    >>> from pyspark.sql.types import StructType, StructField, IntegerType
    >>> my_table = SparkIcebergTable(
    ...     table="my.iceberg.table",
    ...     schema=StructType(
    ...         fields=[
    ...             StructField("id", IntegerType()),
    ...             StructField("amount", IntegerType()),
    ...         ]
    ...     )
    ... )

    >>> import pyspark.sql.functions as F
    >>> my_partitioned_table = (
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
    >>> table_with_properties = SparkIcebergTable(
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

    @staticmethod
    def _parse_partition_by(
        partition_by: SparkIcebergPartitionType,
    ) -> tuple[list[str], list[Column]]:
        """Parses the partition_by argument.

        Args:
            partition_by: columns to partition by

        Returns:
            A tuple containing the list of partition column names and the list
            of partition columns for the writer.

        Raises:
            TypeError: if partition_by is not a supported type
        """
        if not partition_by:
            return [], []

        partition_cols: list[str] = []
        partitions: list[Column] = []

        if isinstance(partition_by, str):
            partition_cols.append(partition_by)
            partitions.append(F.col(partition_by))
        elif isinstance(partition_by, (list, tuple)):
            if all(isinstance(item, str) for item in partition_by):
                partition_cols.extend(partition_by)  # type: ignore[arg-type]
                partitions.extend([F.col(p) for p in partition_by])  # type: ignore[arg-type]
            else:
                for t in partition_by:
                    if not isinstance(t, tuple):
                        raise TypeError(
                            f"Expected partition_by to be a tuple of tuples, "
                            f"got {type(t)}: {t}"
                        )
                    if len(t) == 2 and callable(t[0]):
                        partition_cols.append(t[1])  # ty: ignore[index-out-of-bounds]
                        partitions.append(t[0](t[1]))  # ty: ignore[index-out-of-bounds]
                    elif len(t) == 1 and isinstance(t[0], str):
                        partition_cols.append(t[0])
                        partitions.append(F.col(t[0]))
                    else:
                        raise TypeError(
                            f"Expected partition_by to be a tuple of tuples "
                            f"with either 1 or 2 elements, got {len(t)}: {t}"
                        )
        else:
            raise TypeError(
                f"Unsupported type for partition_by: {type(partition_by)}"
            )
        return partition_cols, partitions

    def _writer(
        self, df: DataFrame, partition_by: SparkIcebergPartitionType
    ) -> "DataFrameWriter":
        """Returns a Spark DataFrame writer configured by save options.

        Args:
            df: DataFrame
            partition_by: columns to partition by

        Returns:
            the writer
        """

        writer = df.writeTo(self.table).using("iceberg")
        for k, v in self.properties:
            writer = writer.tableProperty(k, v)

        if not partition_by:
            return writer

        _, partitions = self._parse_partition_by(partition_by)
        return writer.partitionedBy(*partitions)

    def save(
        self,
        df: DataFrame,
        mode: SparkIcebergWriteMode = "overwritePartitions",
        partition_by: SparkIcebergPartitionType = (),
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
            partition_by: columns to partition by, can be
                - a single column name as a string, e.g. "colour"
                - a list of column names, e.g. ["colour", "dt"]
                - a tuple of tuples for more complex partitioning, e.g.
                  (("colour",), (F.years, "dt"))

        Raises:
            ValueError: if mode is not one of the supported modes
            RuntimeError: if the Spark captured exception cannot be parsed
            CapturedException: if there is an error during the write operation
        """
        df = apply_schema(df, self.schema) if self.schema else df
        if partition_by:
            partition_cols, _ = self._parse_partition_by(partition_by)
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
