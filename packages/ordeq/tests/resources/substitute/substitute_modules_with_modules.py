from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote, remote_extended, inconsistent

print(_build_substitution_map({local: remote, package_base: package_overlay}))
