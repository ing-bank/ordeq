from example_catalogs import local_package
from ordeq._substitute import _build_substitution_map

# Should return an empty map
print(_build_substitution_map({local_package: local_package}))
