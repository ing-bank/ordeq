from collections.abc import Generator
from pathlib import Path
from shutil import rmtree
from tempfile import gettempdir
from typing import cast

import pytest
from ordeq_iceberg import IcebergCatalog
from pyiceberg.catalog import CatalogType
from pyiceberg.catalog.sql import SqlCatalog


@pytest.fixture
def resources_dir(request: pytest.FixtureRequest) -> Path:
    """Loads a `Path` referring to the resources directory specific to the
    requesting test module.

    For example, in tests/test_sth.py, this test should pass:

    >>> def test_method(resources_dir):
    ...     assert resources_dir == "tests/test_sth"

    Can be used to load and save data during tests in its own dedicated
    folder, for instance:

    >>> def test_method(resources_dir):
    ...     with open(resources_dir / "test_method.csv", "r") as file:
    ...         assert len(file.readlines()) == 1

    Args:
        request: the `FixtureRequest` of the requesting test module

    Returns:
        the path to the resources directory
    """

    (test_file_dot_py, _, _) = request.node.location
    test_file = Path(*Path(test_file_dot_py).with_suffix("").parts[3:])
    return Path(__file__).parent / "tests-resources" / test_file


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
