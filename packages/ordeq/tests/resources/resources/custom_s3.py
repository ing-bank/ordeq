# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume a file on S3.
from dataclasses import dataclass

from ordeq import Input
from ordeq_files import CSV
from pathlib import Path


@dataclass(frozen=True)
class S3File:
    bucket: str
    key: str


@dataclass(frozen=True)
class S3Object(Input[bytes]):
    bucket: str
    key: str

    def load(self) -> bytes:
        return b""


s3_file = S3File(bucket="bucket", key="key.csv")
csv_raw = S3Object(bucket=s3_file.bucket, key=s3_file.key) @ s3_file
csv_df = CSV(path=Path(f"s3://{s3_file.bucket}/{s3_file.key}")) @ s3_file

print(csv_raw._resource)
print(csv_df._resource)
