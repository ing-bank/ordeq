# type: ignore
from ordeq import Input

# This inherits from the base catalog:
from example_catalogs.remote import *  # noqa: F403 (import all definitions)

# This overrides the base catalog:
hello: Input[str] = Input("Hey I am overriding the hello IO")
