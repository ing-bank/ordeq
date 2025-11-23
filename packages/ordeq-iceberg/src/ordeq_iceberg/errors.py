"""Module defining custom exceptions for Iceberg-related operations."""


class IcebergError(Exception):
    """Base class for Iceberg-related errors."""


class IcebergTableAlreadyExistsError(IcebergError):
    """Error raised when trying to create a table that already exists."""
