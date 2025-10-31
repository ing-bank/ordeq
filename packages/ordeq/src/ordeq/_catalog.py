from types import ModuleType

from ordeq._fqn import FQN, fqn_to_str
from ordeq._resolve import _resolve_module_to_ios


class CatalogError(Exception): ...


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

    def catalog_key(fqn: FQN, catalog: ModuleType):
        full_name = fqn_to_str(fqn)
        return full_name[len(catalog.__name__) + 1:]

    modules = [a, b, *others]

    # for each catalog, the names (keys) of the IO it defines
    catalogs = [
        {
            catalog_key(fqn, catalog)
            for fqn in _resolve_module_to_ios(catalog)
        }
        for catalog in modules
    ]

    overlap = catalogs[0]
    for module, catalog in zip(modules[1:], catalogs[1:], strict=True):
        if diff := overlap.difference(catalog):
            missing_ios = ", ".join(f"'{io}'" for io in diff)
            raise CatalogError(
                f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
            )
