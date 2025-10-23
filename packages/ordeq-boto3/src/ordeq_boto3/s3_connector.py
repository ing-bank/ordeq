from dataclasses import dataclass

from boto3.resources.base import ServiceResource
from botocore.client import BaseClient
from ordeq import IO


@dataclass(frozen=True)
class S3Connector(IO[BaseClient | ServiceResource]):
    """IO object representing the S3 client or S3 resource.

    Example:

    Using a Boto3 S3 Client:

    ```pycon
    >>> from ordeq_boto3 import S3Connector
    >>> import boto3
    >>> s3_connector = S3Connector(
    ...     connector=boto3.client('s3')
    ... )
    >>> client = s3_connector.load()  # doctest: +SKIP
    ```

    Using a Boto3 S3 Resource:

    ```pycon
    >>> from ordeq_boto3 import S3Connector
    >>> import boto3
    >>> s3_connector = S3Connector(
    ...     connector=boto3.resource('s3')
    ... )
    >>> resource = s3_connector.load()  # doctest: +SKIP
    ```

    """

    connector: BaseClient | ServiceResource

    def __post_init__(self):
        valid_types = (BaseClient, ServiceResource)
        if not isinstance(self.connector, valid_types):
            raise TypeError(
                "Expected connector to be a boto3 client or resource"
            )

    def load(self) -> BaseClient | ServiceResource:
        """Gets the S3 Client or S3 Resource

        Returns:
            The S3 Client or Resource
        """
        return self.connector
