from types import ModuleType

from ordeq._fqn import FQN
from ordeq._resolve import _resolve_package_to_ios


class CatalogError(Exception): ...


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
        return fqn.ref[len(catalog.__name__) + 1 :]

    modules = [base, *others]

    # for each catalog, the names (keys) of the IO it defines
    overlap, *catalogs = [
        {
            catalog_key(FQN(module_name, object_name), catalog)
            for module_name, values in _resolve_package_to_ios(catalog).items()
            for object_name in values
        }
        for catalog in modules
    ]

    for module, catalog in zip(others, catalogs, strict=True):
        if diff := overlap.difference(catalog):
            missing_ios = ", ".join(f"'{io}'" for io in sorted(diff))
            raise CatalogError(
                f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
            )
