from ordeq._substitute import _build_substitution_map
from ordeq import IO
from example_catalogs import local_package

# This is NOK: each key and value need to be of the same type
print(_build_substitution_map({local_package: IO()}))
