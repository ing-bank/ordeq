from example_catalogs import local, package_base, package_overlay, remote
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({local: remote, package_base: package_overlay}))
