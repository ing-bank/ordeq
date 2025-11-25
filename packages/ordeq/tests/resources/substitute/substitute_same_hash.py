from example_catalogs import local
from example_duplicates import duplicate_io_same_hash
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({duplicate_io_same_hash: local}))
print(_substitutes_modules_to_ios({local: duplicate_io_same_hash}))
