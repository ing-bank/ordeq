from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote

# This is OK: 'local' and 'remote' both define the same entries
print(_build_substitution_map({local: remote}))
