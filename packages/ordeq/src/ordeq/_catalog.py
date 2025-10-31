from types import ModuleType
from typing import TypeAlias, TypeVar

from ordeq._fqn import FQN, fqn_to_str
from ordeq._io import AnyIO
from ordeq._resolve import (
    _is_io,
    _is_module,
    _resolve_module_to_ios,
    _resolve_package_to_ios,
)


class CatalogError(Exception): ...


PatchedIO: TypeAlias = dict[AnyIO, AnyIO]


def _name_in_catalog(fqn: FQN, catalog: ModuleType) -> str:
    fqn_str = fqn_to_str(fqn)
    if not fqn_str.startswith(catalog.__name__):
        raise ValueError(
            f"IO '{fqn_str}' does not belong to catalog '{catalog.__name__}'"
        )
    return fqn_str[len(catalog.__name__) + 1 :]


T = TypeVar("T")


def _patch_io(io: dict[T, T]) -> PatchedIO:
    if io is None:
        return {}
    patched_io: PatchedIO = {}
    for key, value in io.items():
        breakpoint()
        patched_io.update(_patch(key, value))
    return patched_io


def _patch(patched: T, patched_by: T) -> PatchedIO:
    if _is_module(patched) and _is_module(patched_by):
        return _patch_catalog_by_catalog(patched, patched_by)
    if _is_io(patched) and _is_io(patched_by):
        return _patch_io_by_io(patched, patched_by)
    raise TypeError(
        f"Cannot patch objects of type "
        f"'{type(patched).__name__}' and "
        f"'{type(patched_by).__name__}'"
    )


def _patch_io_by_io(patched: AnyIO, patched_by: AnyIO) -> PatchedIO:
    return {patched: patched_by}


def _patch_catalog_by_catalog(
    patched: ModuleType, patched_by: ModuleType
) -> PatchedIO:
    """Patches an old catalog with a new one.

    Args:
        patched: The old catalog to patch.
        patched_by: The new catalog to patch with.

    Returns:
        The patched catalog.

    Raises:
        CatalogError: If the catalogs are incompatible.
    """
    io: PatchedIO = {}
    for (patched_fqn, patched_io), (patched_by_fqn, patched_by_io) in zip(
        sorted(_resolve_module_to_ios(patched).items()),
        sorted(_resolve_module_to_ios(patched_by).items()),
        strict=True,
    ):
        patched_name_in_catalog = _name_in_catalog(patched_fqn, patched)
        patched_by_name_in_catalog = _name_in_catalog(
            patched_by_fqn, patched_by
        )
        if patched_name_in_catalog != patched_by_name_in_catalog:
            raise CatalogError(
                f"IO {patched_name_in_catalog} was not found in catalog "
                f"'{patched_by.__name__}'. Cannot patch."
            )
        io[patched_io] = patched_by_io
    return io


def check_catalogs_are_consistent(
    base: ModuleType, *others: ModuleType
) -> None:
    """Utility method to checks if two (or more) catalogs are consistent,
    i.e. if they define the same keys.

    Args:
        base: Base catalog to compare against.
        *others: Additional catalogs to compare.

    Raises:
        CatalogError: If the catalogs are inconsistent,
            i.e. if they define different keys.
    """

    def catalog_key(fqn: FQN, catalog: ModuleType):
        full_name = fqn_to_str(fqn)
        return full_name[len(catalog.__name__) + 1 :]

    modules = [base, *others]

    # for each catalog, the names (keys) of the IO it defines
    catalogs = [
        {catalog_key(fqn, catalog) for fqn in _resolve_package_to_ios(catalog)}
        for catalog in modules
    ]

    overlap = catalogs[0]
    for module, catalog in zip(modules[1:], catalogs[1:], strict=True):
        if diff := overlap.difference(catalog):
            missing_ios = ", ".join(f"'{io}'" for io in sorted(diff))
            raise CatalogError(
                f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
            )
