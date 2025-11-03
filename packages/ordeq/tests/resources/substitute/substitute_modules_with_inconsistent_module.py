from ordeq._substitute import _build_substitution_map

from example_catalogs import local, inconsistent

# NOK: 'inconsistent' contains different entries than 'local'
print(_build_substitution_map({local: inconsistent}))
