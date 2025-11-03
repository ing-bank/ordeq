from ordeq._substitute import _build_substitution_map

from ordeq import IO
from example_catalogs import local

print(_build_substitution_map({IO(): local}))
