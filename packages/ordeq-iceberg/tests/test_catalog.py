from unittest.mock import patch

from pyiceberg.catalog import CatalogType

from ordeq_iceberg import IcebergCatalog


def test_load_catalog_with_literal_catalog_type():
    catalog_input = IcebergCatalog(name="test_catalog", catalog_type="in-memory")
    catalog = catalog_input.load()
    assert catalog.name == "test_catalog"


def test_load_catalog_with_enum_catalog_type():
    catalog_input = IcebergCatalog(
        name="test_catalog", catalog_type=CatalogType.IN_MEMORY
    )
    catalog = catalog_input.load()
    assert catalog.name == "test_catalog"


@patch("ordeq_iceberg.catalog.load_catalog")
def test_load_catalog_is_called_with_correct_parameters(mock_load_catalog):
    catalog_input = IcebergCatalog(
        name="test_catalog", catalog_type="catalog_type_value"
    ).with_load_options(some_option="some_value")
    catalog_input.load()
    mock_load_catalog.assert_called_once_with(
        "test_catalog", type="catalog_type_value", some_option="some_value"
    )
