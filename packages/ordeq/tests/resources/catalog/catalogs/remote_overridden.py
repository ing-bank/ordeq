from ordeq import Input
from ordeq_common import Literal

# 'remote' is the catalog that is overridden
from resources.catalog.catalogs.remote import *  # noqa: F403 (import all definitions)

hello: Input[str] = Literal(
    "Hey I am overriding the hello IO"
)  # this overrides the base catalog
