# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

from example_catalogs import package_overlay
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(package_overlay)
pprint(ios)
