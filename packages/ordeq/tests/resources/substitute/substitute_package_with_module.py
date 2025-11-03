from example_catalogs import local, local_package, package_base
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'local_package' contains the exact same entries as 'local'
print(_substitutes_modules_to_ios({local: local_package}))

# This is NOK, 'package_base' contains different entries than 'local':
print(_substitutes_modules_to_ios({local: package_base}))
