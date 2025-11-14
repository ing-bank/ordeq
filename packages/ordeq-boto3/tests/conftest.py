from collections.abc import Generator

import boto3
import pytest
from boto3.resources.base import ServiceResource
from mypy_boto3_s3 import S3Client
from testcontainers.minio import MinioContainer  # type: ignore[import]


@pytest.fixture(scope="session")
def minio() -> Generator[MinioContainer]:
    container = MinioContainer()
    container.start()
    yield container
    container.stop()


@pytest.fixture(scope="session")
def client(minio: MinioContainer) -> S3Client:
    config = minio.get_config()
    return boto3.client(
        service_name="s3",
        aws_access_key_id=config["access_key"],
        aws_secret_access_key=config["secret_key"],
        endpoint_url="http://" + config["endpoint"],
    )


@pytest.fixture(scope="session")
def resource(minio: MinioContainer) -> ServiceResource:
    config = minio.get_config()
    return boto3.resource(
        service_name="s3",
        aws_access_key_id=config["access_key"],
        aws_secret_access_key=config["secret_key"],
        endpoint_url="http://" + config["endpoint"],
    )


@pytest.fixture(scope="session")
def bucket(client: S3Client) -> str:
    bucket_name = "ordeq-boto3-tests"
    client.create_bucket(Bucket=bucket_name)
    return bucket_name
