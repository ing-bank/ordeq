from unittest.mock import patch

import boto3
import pytest
from boto3.resources.base import ServiceResource
from ordeq_boto3 import S3Resource


def test_load_s3_resource_():
    s3_resource = S3Resource()
    assert s3_resource.load() is not None
    assert s3_resource.load() == boto3.resource("s3")


def test_load_s3_resource_with_env():
    with patch("boto3.resource") as mock_resource:
        s3_resource = S3Resource()
        s3_resource.load(
            endpoint_url="https://custom-endpoint",
            region_name="eu-west-1",
            aws_access_key_id="test-key",
            aws_secret_access_key="test-secret",  # noqa: S106
            aws_session_token="test-token",  # noqa: S106
        )

        mock_resource.assert_called_once_with(
            service_name="s3",
            endpoint_url="https://custom-endpoint",
            region_name="eu-west-1",
            aws_access_key_id="test-key",
            aws_secret_access_key="test-secret",  # noqa: S106
            aws_session_token="test-token",  # noqa: S106
        )


def test_s3_resource_with_load_options():
    with patch("boto3.resource") as mock_resource:
        s3_resource = S3Resource()
        s3_resource_with_opts = s3_resource.with_load_options(
            endpoint_url="https://custom-endpoint-2",
            region_name="eu-east-1",
            aws_access_key_id="test-key",
            aws_secret_access_key="test-secret",  # noqa: S106
            aws_session_token="test-token",  # noqa: S106
        )

        # Should be a new instance
        assert s3_resource is not s3_resource_with_opts

        s3_resource_with_opts.load()

        # Should use the options when calling load()
        mock_resource.assert_called_once_with(
            service_name="s3",
            endpoint_url="https://custom-endpoint-2",
            region_name="eu-east-1",
            aws_access_key_id="test-key",
            aws_secret_access_key="test-secret",  # noqa: S106
            aws_session_token="test-token",  # noqa: S106
        )


@pytest.mark.docker
def test_s3_resource_bucket_integrartion(
    resource: ServiceResource, bucket: str
):
    test_key = "test_bucket_integration"
    data = b"someKey,someValue"
    resource.Bucket(bucket).put_object(Key=test_key, Body=data)

    # Retrieve the object and check its content
    obj = resource.Object(bucket, test_key)
    body = obj.get()["Body"].read()
    assert body == data
