from example_catalogs import package_base, package_inconsistent
from ordeq._substitute import _substitutes_modules_to_ios

# NOK: 'package_inconsistent' contains different entries than 'package_base'
print(_substitutes_modules_to_ios({package_base: package_inconsistent}))
