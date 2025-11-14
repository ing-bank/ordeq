from example_catalogs import inconsistent, local
from ordeq._substitute import _substitutes_modules_to_ios

# NOK: 'inconsistent' contains different entries than 'local'
print(_substitutes_modules_to_ios({local: inconsistent}))
