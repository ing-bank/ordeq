from dataclasses import dataclass

from ordeq import Input
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType

from ordeq_spark.utils import apply_schema


@dataclass(frozen=True, kw_only=True)
class SparkTable(Input[DataFrame]):
    table: str
    schema: StructType | None = None

    def load(self) -> DataFrame:
        df = SparkSession.builder.getOrCreate().table(self.table)
        return apply_schema(df, self.schema) if self.schema else df
