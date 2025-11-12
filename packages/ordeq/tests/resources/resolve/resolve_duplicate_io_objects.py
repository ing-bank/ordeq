# Captures the behaviour when resolving a module containing the same
# object
from pprint import pprint

from example_duplicates import duplicate_io_objects
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(duplicate_io_objects)
pprint(ios)
assert hash(duplicate_io_objects.x) != hash(duplicate_io_objects.y)
