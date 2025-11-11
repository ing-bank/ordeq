# Captures the behaviour when resolving a module containing the same names
# for the same IO.
from pprint import pprint

from example_duplicates import duplicated_io_name
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(duplicated_io_name)
pprint(ios)
