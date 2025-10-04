from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import boto3
from ordeq import IO

if TYPE_CHECKING:
    from mypy_boto3_s3 import S3Client
else:
    S3Client = object


@dataclass(frozen=True, kw_only=True)
class S3Object(IO[bytes]):
    """IO for loading and saving objects from S3 using boto3.

    Example:

    ```pycon
    >>> from ordeq_boto3 import S3Object
    >>> import boto3

    >>> s3_object = S3Object(
    ...     bucket="my-bucket",
    ...     key="path/to/my_object",
    ...     client=boto3.client('s3')
    ... )
    >>> data = s3_object.load()  # doctest: +SKIP

    ```

    Extra parameters can be passed to the `load` and `save` methods, such as:

    ```pycon
    >>> from datetime import datetime
    >>> data = s3_object.load(
    ...     IfModifiedSince=datetime(2015, 1, 1)
    ... )  # doctest: +SKIP
    >>> s3_object.save(ACL="authenticated-read")  # doctest: +SKIP

    ```

    When `client` is not provided, it will be created using
    `boto3.client("s3")`:

    ```pycon
    >>> s3_object = S3Object(
    ...     bucket="my-bucket",
    ...     key="path/to/my_object",
    ... )

    ```

    """

    bucket: str
    key: str
    client: S3Client = field(default_factory=lambda: boto3.client("s3"))

    def load(self, **kwargs) -> bytes:
        response = self.client.get_object(
            Bucket=self.bucket, Key=self.key, **kwargs
        )
        return response["Body"].read()

    def save(self, data: bytes, **kwargs) -> None:
        self.client.put_object(
            Body=data, Bucket=self.bucket, Key=self.key, **kwargs
        )
