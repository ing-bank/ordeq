from ordeq import Input
from ordeq_common import Literal

# This inherits from the base catalog:
from example_catalogs.remote import *  # noqa: F403 (import all definitions)

# This overrides the base catalog:
hello: Input[str] = Literal("Hey I am overriding the hello IO")
