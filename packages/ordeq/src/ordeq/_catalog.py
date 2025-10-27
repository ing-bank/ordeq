from types import ModuleType

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

    # for each catalog, the names (keys) of the IOs it defines
    ios = [
        {name for _, name in _resolve_module_to_ios(catalog)}
        for catalog in [a, b, *others]
    ]

    if not all(s == ios[0] for s in ios[1:]):
        raise CatalogError("Catalogs are inconsistent.")
