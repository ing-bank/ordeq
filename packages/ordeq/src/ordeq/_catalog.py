from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQN, fqn_to_str
from ordeq._io import AnyIO
from ordeq._resolve import _resolve_package_to_ios


class CatalogError(Exception): ...


PatchedIO: TypeAlias = dict[AnyIO, AnyIO]


def _name_in_catalog(fqn: FQN, catalog: ModuleType) -> str:
    fqn_str = fqn_to_str(fqn)
    if not fqn_str.startswith(catalog.__name__):
        raise ValueError(
            f"IO '{fqn_str}' does not belong to catalog '{catalog.__name__}'"
        )
    return fqn_str[len(catalog.__name__) + 1 :]


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
