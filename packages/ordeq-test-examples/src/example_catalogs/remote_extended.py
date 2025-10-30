# type: ignore
from ordeq_common import Print

# This inherits from the base catalog:
from example_catalogs.remote import *  # noqa: F403 (import all definitions)

# This IO is not defined in the base catalog
another_io = Print()
