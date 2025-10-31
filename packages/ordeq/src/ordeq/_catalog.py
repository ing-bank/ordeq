from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQN, fqn_to_str
from ordeq._io import AnyIO
from ordeq._resolve import _resolve_module_to_ios


class CatalogError(Exception): ...


PatchedIO: TypeAlias = dict[AnyIO, AnyIO]


def _name_in_catalog(fqn: FQN, catalog: ModuleType) -> str:
    fqn_str = fqn_to_str(fqn)
    if not fqn_str.startswith(catalog.__name__):
        raise ValueError(
            f"IO '{fqn_str}' does not belong to catalog '{catalog.__name__}'"
        )
    return fqn_str[len(catalog.__name__) + 1:]


def _patch_module_catalog(
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
    a: ModuleType, b: ModuleType, *others: ModuleType
) -> None:
    """Utility method to checks if two (or more) catalogs are consistent,
    i.e. if they define the same keys.

    Args:
        a: First catalog to compare.
        b: Second catalog to compare.
        *others: Additional catalogs to compare.

    Raises:
        CatalogError: If the catalogs are inconsistent,
            i.e. if they define different keys.
    """

    modules = [a, b, *others]

    # for each catalog, the names (keys) of the IO it defines
    catalogs = [
        {
            name_in_catalog(fqn, catalog)
            for fqn in _resolve_module_to_ios(catalog)
        }
        for catalog in modules
    ]

    overlap = catalogs[0]
    for module, catalog in zip(modules[1:], catalogs[1:], strict=True):
        if diff := overlap.difference(catalog):
            missing_ios = ", ".join(f"'{io}'" for io in sorted(diff))
            raise CatalogError(
                f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
            )
