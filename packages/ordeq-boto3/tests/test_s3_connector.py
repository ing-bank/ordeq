import boto3
import pytest
from ordeq_boto3 import S3Connector


def test_it_loads_s3_client():
    client = boto3.client("s3")
    s3_connector = S3Connector(connector=client)
    assert s3_connector.connector is not None
    assert s3_connector.load() == client


def test_it_loads_s3_resource():
    resource = boto3.resource("s3")
    s3_connector = S3Connector(connector=resource)
    assert s3_connector.connector is not None
    assert s3_connector.load() == resource


def test_connector_wrong_type():
    connector = "Hello"
    with pytest.raises(
        TypeError, match="Expected connector to be a boto3 client or resource"
    ):
        S3Connector(connector=connector)


def test_it_raises_if_no_client():
    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'connector'"
    ):
        S3Connector() # ty: ignore[missing-argument]
