from example_catalogs import local, remote_package
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: though 'local' is a file-module and 'remote_package' is a
# package, they both define the same entries and are both of ModuleType.
print(_substitutes_modules_to_ios({local: remote_package}))
