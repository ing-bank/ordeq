from dataclasses import dataclass

from cloudpathlib import CloudPath
from ordeq import Resource
from ordeq._resource import get_resources
from ordeq_boto3 import S3Object
from ordeq_files import CSV


@dataclass(frozen=True)
class S3File(Resource):
    bucket: str
    key: str


s3_file = S3File(bucket="bucket", key="key.csv")
csv_raw = s3_file.add_io(S3Object(bucket=s3_file.bucket, key=s3_file.key))
csv_df = s3_file.add_io(
    CSV(path=CloudPath(f"s3://{s3_file.bucket}/{s3_file.key}"))
)

print(get_resources(csv_raw))
print(get_resources(csv_df))
