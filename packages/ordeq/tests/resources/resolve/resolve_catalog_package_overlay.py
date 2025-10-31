# Captures the behaviour when resolving a package catalog to IO.
from example_catalogs import package_overlay
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(package_overlay)
print(ios)
