from example_catalogs import local
from ordeq._substitute import _substitutes_modules_to_ios

# Should return an empty map
print(_substitutes_modules_to_ios({local: local}))
