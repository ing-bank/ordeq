from ordeq._substitute import _build_substitution_map

from example_catalogs import package_base, package_overlay, \
    package_inconsistent

# This is OK: 'package_overlay' contains all entries of 'package_base'
print(_build_substitution_map({package_base: package_overlay}))

# This is NOK: 'package_base' is not a subset of 'package_inconsistent'
print(_build_substitution_map({package_base: package_inconsistent}))
