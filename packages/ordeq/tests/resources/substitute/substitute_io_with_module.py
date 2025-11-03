from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _build_substitution_map

print(_build_substitution_map({IO(): local}))
