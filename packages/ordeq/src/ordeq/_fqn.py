"""Object references to fully qualified names (FQNs) conversion utilities.

Object references are represented as strings in the format "module:name",
while fully qualified names (FQNs) are represented as tuples of the form
(module, name).
"""

from __future__ import annotations

from typing import TypeAlias

FQN: TypeAlias = tuple[str, str]


def str_to_fqn(name: str) -> FQN:
    """Convert a string representation to a fully qualified name (FQN).

    Args:
        name: A string in the format "module:name".

    Returns:
        A tuple representing the fully qualified name (module, name).

    Raises:
        ValueError: If the input string is not in the expected format.
    """
    if ":" not in name:
        raise ValueError(
            f"Invalid object reference: '{name}'. "
            f"Expected format 'module:name'."
        )
    module_name, _, obj_name = name.partition(":")
    return module_name, obj_name


def fqn_to_str(name: FQN) -> str:
    """Convert a fully qualified name (FQN) to a string representation.

    Args:
        name: A tuple representing the fully qualified name (module, name).

    Returns:
        A string in the format "module:name".
    """
    return f"{name[0]}:{name[1]}"
