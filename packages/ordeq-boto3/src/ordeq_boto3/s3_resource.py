from dataclasses import dataclass
from typing import Any

import boto3
from boto3.resources.base import ServiceResource
from ordeq import Input


@dataclass(frozen=True)
class S3Resource(Input[ServiceResource]):
    """IO object that establishes a boto3 S3 resource connection on load.

    Example:

    ```pycon
    >>> from ordeq_boto3 import S3Resource
    >>> import os
    >>> s3_resource = S3Resource()
    >>> resource = s3_resource.load(
    ...     endpoint_url=os.getenv("AWS_S3_ENDPOINT_URL"),
    ...     region_name=os.getenv("AWS_DEFAULT_REGION"),
    ...     aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    ...     aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    ...     aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    ... )

    ```
    """

    def load(self, **load_options: Any) -> ServiceResource:
        """Establishes and returns a boto3 S3 resource.

        Args:
            load_options: Additional options to pass to boto3.resource

        Returns:
            The S3 ServiceResource
        """
        return boto3.resource(service_name="s3", **load_options)
