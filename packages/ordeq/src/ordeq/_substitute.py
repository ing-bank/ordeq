"""Functionality to substitute IOs in an Ordeq project.

IOs are substituted based on a mapping provided by the user. This allows for
flexible reconfiguration of IO without modifying the pipeline code.
"""

from types import ModuleType
from typing import TypeVar

from ordeq._catalog import check_catalogs_are_consistent
from ordeq._io import AnyIO
from ordeq._resolve import _is_io, _is_module, _resolve_package_to_ios

T = TypeVar("T", bound=AnyIO | ModuleType)

IOSubstitutionMap = dict[AnyIO, AnyIO]


def _build_substitution_map(io: dict[T, T]) -> IOSubstitutionMap:
    if io is None:
        return {}
    substitution_map: IOSubstitutionMap = {}
    for key, value in io.items():
        substitution_map.update(_build_substitute(key, value))
    return substitution_map


def _build_substitute(old: T, new: T) -> IOSubstitutionMap:
    if _is_module(old) and _is_module(new):
        return _substitute_catalog_by_catalog(old, new)
    if _is_io(old) and _is_io(new):
        return _substitute_io_by_io(old, new)
    raise TypeError(
        f"Cannot substitute objects of type "
        f"'{type(old).__name__}' and "
        f"'{type(new).__name__}'"
    )


def _substitute_io_by_io(
    patched: AnyIO, patched_by: AnyIO
) -> IOSubstitutionMap:
    return {patched: patched_by}


def _substitute_catalog_by_catalog(
    old: ModuleType, new: ModuleType
) -> IOSubstitutionMap:
    check_catalogs_are_consistent(old, new)
    io: IOSubstitutionMap = {}
    for (_, old_io), (_, new_io) in zip(
        sorted(_resolve_package_to_ios(old).items()),
        sorted(_resolve_package_to_ios(new).items()),
        strict=True,
    ):
        io[old_io] = new_io
    return io
