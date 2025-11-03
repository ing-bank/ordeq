from example_catalogs import local, remote
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'local' and 'remote' both define the same entries
print(_substitutes_modules_to_ios({local: remote}))
