from unittest.mock import Mock, patch

import pytest
from ordeq import IOException
from ordeq_iceberg import IcebergGlueCatalog, IcebergInMemoryCatalog
from pyiceberg.catalog.glue import GlueCatalog
from pyiceberg.catalog.memory import InMemoryCatalog


class TestIcebergGlueCatalog:
    """Test the IcebergGlueCatalog Input class."""

    def test_initialization(self):
        """Test that IcebergGlueCatalog can be initialized with a name."""
        catalog = IcebergGlueCatalog(name="test_catalog")
        assert catalog.name == "test_catalog"

    def test_load_returns_glue_catalog(self):
        """Test that load returns a GlueCatalog instance."""
        catalog = IcebergGlueCatalog(name="test_catalog")

        # Mock the GlueCatalog creation to avoid actual AWS calls
        with patch("ordeq_iceberg.catalog.GlueCatalog") as mock_glue:
            mock_instance = Mock(spec=GlueCatalog)
            mock_glue.return_value = mock_instance

            result = catalog.load()

            # Verify GlueCatalog was called with correct parameters
            mock_glue.assert_called_once_with(name="test_catalog")
            assert result == mock_instance

    def test_load_with_load_options(self):
        """Test that load passes additional options to GlueCatalog."""
        catalog = IcebergGlueCatalog(name="test_catalog")

        with patch("ordeq_iceberg.catalog.GlueCatalog") as mock_glue:
            mock_instance = Mock(spec=GlueCatalog)
            mock_glue.return_value = mock_instance

            # Test with additional load options
            result = catalog.load(
                region_name="us-west-2", aws_access_key_id="test_key"
            )

            # Verify GlueCatalog was called with all parameters
            mock_glue.assert_called_once_with(
                name="test_catalog",
                region_name="us-west-2",
                aws_access_key_id="test_key",
            )
            assert result == mock_instance

    def test_load_error_handling(self):
        """Test that load errors are wrapped in IOException."""
        catalog = IcebergGlueCatalog(name="test_catalog")

        with patch("ordeq_iceberg.catalog.GlueCatalog") as mock_glue:
            # Make GlueCatalog raise an exception
            mock_glue.side_effect = Exception("AWS connection failed")

            # Verify IOException is raised
            with pytest.raises(IOException) as exc_info:
                catalog.load()

            assert "Failed to load" in str(exc_info.value)
            assert "AWS connection failed" in str(exc_info.value)


class TestIcebergInMemoryCatalog:
    """Test the IcebergInMemoryCatalog Input class."""

    def test_initialization(self):
        """Test that IcebergInMemoryCatalog can be initialized with a name."""
        catalog = IcebergInMemoryCatalog(name="test_catalog")
        assert catalog.name == "test_catalog"

    def test_load_returns_inmemory_catalog(self):
        """Test that load returns an InMemoryCatalog instance."""
        catalog = IcebergInMemoryCatalog(name="test_catalog")

        result = catalog.load()

        # Verify it returns an InMemoryCatalog instance
        assert isinstance(result, InMemoryCatalog)
        assert result.name == "test_catalog"


class TestCatalogIntegration:
    """Integration tests for both catalog types."""

    def test_catalog_name_required(self):
        """Test that catalog name is required for both types."""
        # Should raise TypeError if name is not provided
        with pytest.raises(TypeError):
            IcebergGlueCatalog()  # type: ignore

        with pytest.raises(TypeError):
            IcebergInMemoryCatalog()  # type: ignore
