from collections.abc import Callable, Generator
from io import BytesIO

import pytest
from cloudpathlib import CloudPath, S3Client
from minio import Minio
from minio.helpers import ObjectWriteResult
from testcontainers.minio import MinioContainer


@pytest.fixture(scope="session")
def minio() -> Generator[MinioContainer]:
    container = MinioContainer()
    container.start()
    yield container
    container.stop()


@pytest.fixture(scope="session")
def minio_client(minio: MinioContainer) -> Minio:
    return minio.get_client()


@pytest.fixture(scope="session")
def minio_bucket(minio_client: Minio) -> str:
    minio_client.make_bucket("tests-resources")
    return "tests-resources"


@pytest.fixture(scope="session")
def minio_config(minio: MinioContainer) -> dict:
    return minio.get_config()


@pytest.fixture(scope="session")
def minio_cloudpath(
    minio_bucket: str, minio_config: dict
) -> Callable[[str], CloudPath]:
    """Creates a CloudPath instance that connects to the MinIO storage.

    Args:
        minio_bucket: the bucket used to store test data
        minio_config: connection configuration

    Returns:
        the CloudPath
    """

    return lambda key: CloudPath(
        f"s3://{minio_bucket}/{key}",
        client=S3Client(
            aws_access_key_id=minio_config["access_key"],
            aws_secret_access_key=minio_config["secret_key"],
            endpoint_url="http://" + minio_config["endpoint"],
        ),
    )


@pytest.fixture(scope="session")
def minio_put_object(
    minio_client: Minio, minio_bucket: str
) -> Callable[[str, bytes], ObjectWriteResult]:
    """Returns a method that puts an object to MinIO storage. Used to seed
    test data.

    Args:
        minio_client: the client to the MinIO service
        minio_bucket: the bucket used to store data.

    Returns:
        method that gets puts an object
    """

    return lambda key, data: minio_client.put_object(
        minio_bucket, key, BytesIO(data), length=len(data)
    )


@pytest.fixture(scope="session")
def minio_get_object(minio_client: Minio, minio_bucket: str):
    """Returns a method that gets an object from MinIO storage.

    Args:
        minio_client: the client to the MinIO service
        minio_bucket: the bucket used to store test data.

    Returns:
        method that gets an object
    """

    def get(key: str):
        return minio_client.get_object(minio_bucket, key)

    return get
