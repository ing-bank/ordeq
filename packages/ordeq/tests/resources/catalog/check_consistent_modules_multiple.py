from example_catalogs import local, remote, remote_overridden
from ordeq import check_catalogs_are_consistent

check_catalogs_are_consistent(local, remote, remote_overridden)
