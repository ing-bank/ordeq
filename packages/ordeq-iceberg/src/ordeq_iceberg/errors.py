"""Module defining custom exceptions for Iceberg-related operations."""

from ordeq import IOException


class IcebergIOError(IOException):
    """Base class for Iceberg-related errors."""


class IcebergTableAlreadyExistsError(IcebergIOError):
    """Error raised when trying to create a table that already exists."""
