"""Functionality to substitute IOs in an Ordeq project.

IOs are substituted based on a mapping provided by the user. This allows for
flexible reconfiguration of IO without modifying the pipeline code.
"""

from types import ModuleType

from ordeq._catalog import CatalogError
from ordeq._io import AnyIO, _is_io
from ordeq._resolve import _is_module, _resolve_package_to_ios

IOSubs = dict[AnyIO, AnyIO]


def _substitute_catalog_by_catalog(
    old: ModuleType, new: ModuleType, requested: set[AnyIO] | None = None
) -> IOSubs:
    io: IOSubs = {}
    old_catalog = dict(sorted(_resolve_package_to_ios(old).items()))
    new_catalog = dict(sorted(_resolve_package_to_ios(new).items()))
    requested_ = requested or set()
    for old_ios, new_ios in zip(
        old_catalog.values(), new_catalog.values(), strict=False
    ):
        for name, old_io in old_ios.items():
            if name not in new_ios:
                if requested_ and old_io not in requested_:
                    continue
                raise CatalogError(
                    f"Catalog '{new.__name__}' is missing IO '{name}' "
                )
            io[old_io] = new_ios[name]
    return io


def _substitutes_modules_to_ios(
    io: dict[AnyIO | ModuleType, AnyIO | ModuleType],
    requested: set[AnyIO] | None = None,
) -> IOSubs:
    substitution_map: IOSubs = {}
    for old, new in io.items():
        if _is_module(old) and _is_module(new):
            substitution_map.update(
                _substitute_catalog_by_catalog(old, new, requested)
            )
        elif _is_io(old) and _is_io(new):
            # (ty false positive)
            substitution_map[old] = new  # type: ignore[invalid-assignment]
        else:
            raise TypeError(
                f"Cannot substitute objects of type "
                f"'{type(old).__name__}' and "
                f"'{type(new).__name__}'"
            )
    return substitution_map
