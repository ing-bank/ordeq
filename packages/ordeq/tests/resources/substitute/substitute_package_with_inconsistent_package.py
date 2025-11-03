from example_catalogs import package_base, package_inconsistent
from ordeq._substitute import _build_substitution_map

# NOK: 'package_inconsistent' contains different entries than 'package_base'
print(_build_substitution_map({package_base: package_inconsistent}))
