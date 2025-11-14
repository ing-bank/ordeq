from collections.abc import Hashable
from dataclasses import dataclass


@dataclass(frozen=True)
class Resource:
    """Utility class to represent IO resources during graph building.
    Eases type checking, comparison and representation."""

    value: Hashable

    def __repr__(self) -> str:
        return repr(self.value)
