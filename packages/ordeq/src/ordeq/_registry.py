from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ordeq._nodes import Node

from collections.abc import Hashable
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Registry(Generic[T]):
    """Class representing a registry of objects."""

    _data: dict[Hashable, T] = field(default_factory=dict, init=False)

    def get(self, key: Hashable) -> T:
        """Retrieve the value associated with the given key.

        Args:
            key: The key to look up in the registry.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the registry.
        """  # noqa: DOC502 (Raised exception is not explicitly raised)

        return self._data[key]

    def set(self, key: Hashable, value: T) -> None:
        """Add a new key-value pair to the registry.

        Args:
            key: The key to add to the registry.
            value: The value to associate with the key.

        Raises:
            KeyError: If the key already exists in the registry.
        """

        if key in self._data:
            raise KeyError(f"Key '{key}' already exists")
        self._data[key] = value

    def __contains__(self, key: Hashable) -> bool:
        """Check if the item exists in the registry.

        Args:
            key: The key to check for existence.

        Returns:
            True if the key exists, False otherwise.
        """

        return key in self._data


# Global node registry used by Ordeq. Users should not use this directly.
NODE_REGISTRY: Registry[Node] = Registry()
