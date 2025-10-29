from ordeq_common import Print

# 'remote' is the catalog that is extended
from resources.catalog.catalogs.remote import *  # noqa: F403 (import all definitions)

another_io = Print()  # this IO is not defined in the base catalog
