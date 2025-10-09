from types import ModuleType

from ordeq.io import IO, Input, Output


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

    ios = []  # for each catalog, the names (keys) of the IOs it defines
    for catalog in [a, b, *others]:
        catalog_ios = set()
        for key, value in vars(catalog).items():
            if isinstance(value, (IO, Input, Output)):
                catalog_ios.add(key)
        ios.append(catalog_ios)

    if not all(s == ios[0] for s in ios[1:]):
        raise CatalogError("Catalogs are inconsistent.")
