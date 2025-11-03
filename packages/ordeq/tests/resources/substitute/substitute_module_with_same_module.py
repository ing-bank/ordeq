from example_catalogs import local
from ordeq._substitute import _build_substitution_map

# Should return an empty map
print(_build_substitution_map({local: local}))
