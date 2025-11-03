from example_catalogs import local, package_base, package_overlay, remote
from ordeq._substitute import _build_substitution_map

print(_build_substitution_map({local: remote, package_base: package_overlay}))
