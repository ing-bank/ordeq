from ordeq._substitute import _build_substitution_map

from example_catalogs import local, local_package, package_base

# This is OK: 'local_package' contains the exact same entries as 'local'
print(_build_substitution_map({local: local_package}))

# This is NOK, 'package_base' contains different entries than 'local':
print(_build_substitution_map({local: package_base}))
