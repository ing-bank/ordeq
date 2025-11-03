from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios

# This is NOK: cannot substitute IO with module
print(_substitutes_modules_to_ios({IO(): local}))
