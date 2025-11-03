from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _build_substitution_map

# This is NOK: each key and value need to be of the same type
print(_build_substitution_map({local: IO()}))
