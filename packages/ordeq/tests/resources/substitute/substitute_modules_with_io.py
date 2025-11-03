from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios

# This is NOK: each key and value need to be of the same type
print(_substitutes_modules_to_ios({local: IO()}))
