# Captures the behaviour when resolving a module containing duplicate IOs
# created via the .copy() method.
from pprint import pprint

from example_duplicates import duplicate_io_via_copy
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(duplicate_io_via_copy)
pprint(ios)
