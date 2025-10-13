from collections.abc import Callable
from pathlib import Path

import pytest
import yaml
from cloudpathlib import CloudPath
from minio.helpers import ObjectWriteResult
from ordeq_yaml import YAML
from urllib3 import BaseHTTPResponse


class TestYAMLLocal:
    def test_it_loads(self, tmp_path: Path):
        path = tmp_path / "test_it_loads.yaml"
        data = {"someKey": "someValue"}
        with path.open(mode="w") as fh:
            yaml.safe_dump(data, fh)
        assert YAML(path=path).load() == data

    def test_it_saves(self, tmp_path: Path):
        path = tmp_path / "test_it_saves.yaml"
        data = {"someKey": "someValue"}
        YAML(path=path).save(data)
        with path.open(mode="r") as file:
            assert yaml.safe_load(file) == data


class TestYAMLMinio:
    @pytest.mark.docker
    def test_it_loads(
        self,
        minio_put_object: Callable[[str, bytes], ObjectWriteResult],
        minio_cloudpath: Callable[[str], CloudPath],
    ):
        key = "TestYAMLMinio/test_it_loads.yaml"
        data = {"someKey": "someValue"}
        minio_put_object(key, yaml.dump(data).encode("utf-8"))
        assert YAML(path=minio_cloudpath(key)).load() == data

    @pytest.mark.docker
    def test_it_saves(
        self,
        minio_cloudpath: Callable[[str], CloudPath],
        minio_get_object: Callable[[str], BaseHTTPResponse],
    ):
        key = "TestYAMLMinio/test_it_saves.yaml"
        data = {"someKey": "someValue"}
        YAML(path=minio_cloudpath(key)).save(data)
        assert yaml.full_load(minio_get_object(key)) == data
