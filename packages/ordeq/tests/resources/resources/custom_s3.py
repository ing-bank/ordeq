# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume a file on S3.
from dataclasses import dataclass

from cloudpathlib import CloudPath
from ordeq import Input
from ordeq._io import get_resource
from ordeq_files import CSV


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
csv_df = CSV(path=CloudPath(f"s3://{s3_file.bucket}/{s3_file.key}")) @ s3_file

print(get_resource(csv_raw))
print(get_resource(csv_df))
