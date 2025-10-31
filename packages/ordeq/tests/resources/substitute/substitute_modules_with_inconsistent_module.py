from ordeq._substitute import _build_substitution_map

from example_catalogs import local, inconsistent

print(_build_substitution_map({local: inconsistent}))
