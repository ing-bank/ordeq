from example_catalogs import inconsistent, local
from ordeq._substitute import _build_substitution_map

# NOK: 'inconsistent' contains different entries than 'local'
print(_build_substitution_map({local: inconsistent}))
