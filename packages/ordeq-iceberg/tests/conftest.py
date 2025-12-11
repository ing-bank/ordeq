from collections.abc import Generator
from pathlib import Path
from shutil import rmtree
from tempfile import gettempdir
from typing import cast

import pytest
from ordeq_iceberg import IcebergCatalog
from pyiceberg.catalog import CatalogType
from pyiceberg.catalog.sql import SqlCatalog


@pytest.fixture(scope="module")
def sql_catalog_io() -> Generator[IcebergCatalog]:
    temp_path = Path(gettempdir())
    catalog_path = temp_path / "test_sql_catalog"
    catalog_path.mkdir(parents=True, exist_ok=True)
    catalog_io = IcebergCatalog(
        name="test_sql_catalog", catalog_type=CatalogType.SQL
    ).with_load_options(
        uri=f"sqlite:///{catalog_path / 'iceberg.db'}",
        warehouse=str(catalog_path / "warehouse"),
    )
    catalog = cast("SqlCatalog", catalog_io.load())
    catalog.create_namespace("test_namespace")
    yield catalog_io
    catalog.close()
    (catalog_path / "iceberg.db").unlink(missing_ok=True)
    rmtree(catalog_path / "warehouse", ignore_errors=True)
    catalog_path.rmdir()


@pytest.fixture(scope="module")
def sql_catalog(sql_catalog_io: IcebergCatalog) -> Generator[SqlCatalog]:
    catalog = cast("SqlCatalog", sql_catalog_io.load())
    yield catalog
    catalog.close()
