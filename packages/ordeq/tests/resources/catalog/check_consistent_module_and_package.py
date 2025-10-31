from example_catalogs import local, local_package
from ordeq import check_catalogs_are_consistent

# Should pass without errors:
check_catalogs_are_consistent(local, local_package)

# Should pass without errors:
check_catalogs_are_consistent(local_package, local)
