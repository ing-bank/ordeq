from dataclasses import dataclass

from ordeq import Input
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType


@dataclass(frozen=True, kw_only=True)
class SparkTable(Input[DataFrame]):
    table: str
    schema: StructType | None = None

    def load(self) -> DataFrame:
        return SparkSession.builder.getOrCreate().table(self.table)
