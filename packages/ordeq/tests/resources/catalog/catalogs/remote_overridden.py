from ordeq import Input
from resources.catalog.catalogs.remote import *  # 'remote' is the catalog that is overridden

from ordeq_common import Literal

hello: Input[str] = Literal("Hey I am overriding the hello IO")  # this overrides the base catalog
