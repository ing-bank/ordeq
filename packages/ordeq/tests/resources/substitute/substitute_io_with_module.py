from ordeq._substitute import _build_substitution_map

from example_catalogs import local
from ordeq import IO

print(_build_substitution_map({local: IO()}))
