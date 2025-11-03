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

IOSubstitutes = dict[AnyIO, AnyIO]


def _substitute_io_by_io(
    patched: AnyIO, patched_by: AnyIO
) -> IOSubstitutes:
    if patched == patched_by:
        return {}
    return {patched: patched_by}


def _substitute_catalog_by_catalog(
    old: ModuleType, new: ModuleType
) -> IOSubstitutes:
    if old == new:
        return {}
    check_catalogs_are_consistent(old, new)
    io: IOSubstitutes = {}
    for (_, old_io), (_, new_io) in zip(
        sorted(_resolve_package_to_ios(old).items()),
        sorted(_resolve_package_to_ios(new).items()),
        strict=True,
    ):
        io[old_io] = new_io
    return io


def _substitute(old: T, new: T) -> IOSubstitutes:
    if _is_module(old) and _is_module(new):
        return _substitute_catalog_by_catalog(old, new)
    if _is_io(old) and _is_io(new):
        return _substitute_io_by_io(old, new)
    raise TypeError(
        f"Cannot substitute objects of type "
        f"'{type(old).__name__}' and "
        f"'{type(new).__name__}'"
    )


def _substitutes_modules_to_ios(io: dict[T, T] | None) -> IOSubstitutes:
    if io is None:
        return {}
    substitution_map: IOSubstitutes = {}
    for key, value in io.items():
        substitution_map.update(_substitute(key, value))
    return substitution_map
