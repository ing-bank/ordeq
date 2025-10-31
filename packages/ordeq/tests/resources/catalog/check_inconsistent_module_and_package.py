from example_catalogs import (
    package_base, remote
)

from ordeq import check_catalogs_are_consistent

# Should raise CatalogError:
check_catalogs_are_consistent(
    remote, package_base
)
