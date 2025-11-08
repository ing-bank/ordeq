## Resource

```python
# Captures how resources can be used to distinguish between two IO
# distinct implementations that both consume a file on S3.
from dataclasses import dataclass

from cloudpathlib import CloudPath
from ordeq_boto3 import S3Object
from ordeq_files import CSV


@dataclass(frozen=True)
class S3File:
    bucket: str
    key: str


s3_file = S3File(bucket="bucket", key="key.csv")
csv_raw = S3Object(bucket=s3_file.bucket, key=s3_file.key) @ s3_file
csv_df = CSV(path=CloudPath(f"s3://{s3_file.bucket}/{s3_file.key}")) @ s3_file

print(csv_raw.resources)
print(csv_df.resources)

```

## Output

```text
{S3File(bucket='bucket', key='key.csv')}
{S3File(bucket='bucket', key='key.csv')}

```