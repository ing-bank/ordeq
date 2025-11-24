"""Object references to fully qualified names (FQNs) conversion utilities.

Object references are represented as strings in the format "module:name",
while fully qualified names (FQNs) are represented as tuples of the form
(module, name).
"""

from __future__ import annotations

from typing import (
    Annotated,
    Literal,
    NamedTuple,
    TypeAlias,
    TypeGuard,
    TypeVar,
)

ModuleName: TypeAlias = Annotated[
    str, "Name of a module: 'module.submodule.[...]"
]
ObjectName: TypeAlias = Annotated[str, "Name of an object within a module"]
T = TypeVar("T")
ObjectRef: TypeAlias = Annotated[
    str, "Reference to an object: 'module.submodule.[...]:name'"
]


def is_object_ref(string: str) -> TypeGuard[ObjectRef]:
    return ":" in string


def object_ref_to_fqn(ref: ObjectRef) -> tuple[ModuleName, ObjectName]:
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


def fqn_to_object_ref(fqn: tuple[ModuleName, ObjectName]) -> ObjectRef:
    """Convert a fully qualified name (FQN) to a string representation.

    Args:
        fqn: A tuple representing the fully qualified name (module, name).

    Returns:
        A string in the format "module:name".
    """
    return f"{fqn[0]}:{fqn[1]}"


class FQN(NamedTuple):
    module: ModuleName
    name: ObjectName

    @classmethod
    def from_ref(cls, ref: ObjectRef) -> FQN:
        """Create an FQN from a string representation.

        Args:
            ref: A string in the format "module:name".

        Returns:
            A tuple representing the fully qualified name (module, name).
        """
        fqn = object_ref_to_fqn(ref)
        return FQN(module=fqn[0], name=fqn[1])

    @property
    def ref(self) -> ObjectRef:
        """Get the string representation of the fully qualified name (FQN).

        Returns:
            A string in the format "module:name".
        """
        return fqn_to_object_ref(self)

    def __str__(self) -> str:
        return format(self, "ref")

    def __format__(self, format_spec: Literal["ref", "desc"] = "ref") -> str:  # type: ignore[override]
        if format_spec == "ref":
            return self.ref
        return f"'{self.name}' in module '{self.module}'"


FQ: TypeAlias = tuple[FQN, T]
AnyRef: TypeAlias = ModuleName | ObjectRef
Unknown: str = "unknown"
