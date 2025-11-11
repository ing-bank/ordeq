"""Object references to fully qualified names (FQNs) conversion utilities.

Object references are represented as strings in the format "module:name",
while fully qualified names (FQNs) are represented as tuples of the form
(module, name).
"""

from __future__ import annotations

from typing import Annotated, TypeAlias, TypeGuard, TypeVar

ModuleRef: TypeAlias = Annotated[
    str, "Reference to a module: 'module.submodule.[...]"
]
FQN: TypeAlias = tuple[ModuleRef, str]
T = TypeVar("T")
FQNamed: TypeAlias = tuple[ModuleRef, str, T]
ObjectRef: TypeAlias = Annotated[
    str, "Reference to an object: 'module.submodule.[...]:name'"
]
AnyRef: TypeAlias = ModuleRef | ObjectRef


def is_object_ref(string: str) -> TypeGuard[ObjectRef]:
    return ":" in string


def object_ref_to_fqn(ref: ObjectRef) -> FQN:
    """Convert a string representation to a fully qualified name (FQN).

    Args:
        ref: A string in the format "module:name".

    Returns:
        A tuple representing the fully qualified name (module, name).

    Raises:
        ValueError: If the input string is not in the expected format.
    """
    if not is_object_ref(ref):
        raise ValueError(
            f"Invalid object reference: '{ref}'. "
            f"Expected format 'module:name'."
        )
    module_name, _, obj_name = ref.partition(":")
    return module_name, obj_name


def fqn_to_object_ref(name: FQN) -> ObjectRef:
    """Convert a fully qualified name (FQN) to a string representation.

    Args:
        name: A tuple representing the fully qualified name (module, name).

    Returns:
        A string in the format "module:name".
    """
    return f"{name[0]}:{name[1]}"
