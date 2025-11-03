from example_catalogs import (
    package_base,
    package_inconsistent,
    package_overlay,
)
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'package_overlay' contains all entries of 'package_base'
print(_substitutes_modules_to_ios({package_base: package_overlay}))

# This is NOK: 'package_base' is not a subset of 'package_inconsistent'
print(_substitutes_modules_to_ios({package_base: package_inconsistent}))
