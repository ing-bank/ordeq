"""Functionality to substitute IOs in an Ordeq project.

IOs are substituted based on a mapping provided by the user. This allows for
flexible reconfiguration of IO without modifying the pipeline code.
"""

from types import ModuleType

from ordeq._catalog import check_catalogs_are_consistent
from ordeq._fqn import AnyRef, is_object_ref
from ordeq._io import AnyIO
from ordeq._resolve import (
    _is_io,
    _is_module,
    _resolve_module_ref_to_module,
    _resolve_object_ref_to_io,
    _resolve_package_to_ios,
)

IOSubstitutes = dict[AnyIO, AnyIO]


def _resolve_refs_to_subs(
    subs: dict[AnyRef | AnyIO | ModuleType, AnyRef | AnyIO | ModuleType],
) -> dict[AnyIO | ModuleType, AnyIO | ModuleType]:
    def resolve_ref_to_sub(ref: AnyRef) -> AnyIO | ModuleType:
        if is_object_ref(ref):
            _, _, io = _resolve_object_ref_to_io(ref)
            return io
        return _resolve_module_ref_to_module(ref)

    subs_ = {}
    for old, new in subs.items():
        old_sub = resolve_ref_to_sub(old) if isinstance(old, str) else old
        new_sub = resolve_ref_to_sub(new) if isinstance(new, str) else new
        subs_[old_sub] = new_sub
    return subs_


def _substitute_catalog_by_catalog(
    old: ModuleType, new: ModuleType
) -> IOSubstitutes:
    check_catalogs_are_consistent(old, new)
    io: IOSubstitutes = {}
    old_catalog = dict(sorted(_resolve_package_to_ios(old).items()))
    new_catalog = dict(sorted(_resolve_package_to_ios(new).items()))
    for old_ios, new_ios in zip(
        old_catalog.values(), new_catalog.values(), strict=True
    ):
        for name, old_io in old_ios.items():
            io[old_io] = new_ios[name]
    return io


def _substitutes_modules_to_ios(
    io: dict[AnyIO | ModuleType, AnyIO | ModuleType],
) -> IOSubstitutes:
    substitution_map: IOSubstitutes = {}
    for old, new in io.items():
        if old == new:
            continue
        if _is_module(old) and _is_module(new):
            substitution_map.update(_substitute_catalog_by_catalog(old, new))
        elif _is_io(old) and _is_io(new):
            substitution_map[old] = new
        else:
            raise TypeError(
                f"Cannot substitute objects of type "
                f"'{type(old).__name__}' and "
                f"'{type(new).__name__}'"
            )
    return substitution_map
