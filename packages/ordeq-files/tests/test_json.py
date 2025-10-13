import json
from collections.abc import Callable
from pathlib import Path

import pytest
from cloudpathlib import CloudPath
from minio.helpers import ObjectWriteResult
from ordeq_files import JSON
from urllib3 import BaseHTTPResponse


class TestJSONLocal:
    def test_it_loads(self, tmp_path: Path):
        data = {"someKey": "someValue e, è, é, ê, ë"}
        path = tmp_path / "test_it_loads.json"
        with path.open(mode="w") as fh:
            json.dump(data, fh)
        assert JSON(path=path).load() == data

    def test_it_saves(self, tmp_path: Path):
        path = tmp_path / "test_it_saves.json"
        data = {"someKey": "someValue - e, è, é, ê, ë"}
        JSON(path=path).save(data)
        with path.open(mode="r") as fh:
            assert json.load(fh) == data


class TestJSONMinio:
    @pytest.mark.docker
    def test_it_loads(
        self,
        minio_put_object: Callable[[str, bytes], ObjectWriteResult],
        minio_cloudpath: Callable[[str], CloudPath],
    ):
        key = "TestJSONMinio/test_it_loads.json"
        data = {"someKey": "someValue"}
        minio_put_object(key, json.dumps(data).encode("utf-8"))
        assert JSON(path=minio_cloudpath(key)).load() == data

    @pytest.mark.docker
    def test_it_saves(
        self,
        minio_cloudpath: Callable[[str], CloudPath],
        minio_get_object: Callable[[str], BaseHTTPResponse],
    ):
        key = "TestJSONMinio/test_it_saves.json"
        data = {"someKey": "someValue"}
        JSON(path=minio_cloudpath(key)).save(data)
        assert json.loads(minio_get_object(key).read()) == data
