from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote

print(_build_substitution_map({local: remote}))
