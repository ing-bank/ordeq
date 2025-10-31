from example_catalogs import (
    package_base,
    package_inconsistent,
    package_overlay,
)
from ordeq import check_catalogs_are_consistent

# Should raise CatalogError:
check_catalogs_are_consistent(
    package_base, package_overlay, package_inconsistent
)
