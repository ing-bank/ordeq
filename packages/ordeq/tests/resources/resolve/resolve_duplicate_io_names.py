# Captures the behaviour when resolving a module containing the same names
# for the same IO.
from example_duplicates import duplicate_io_names
from ordeq._resolve import _resolve_module_to_ios

_ = _resolve_module_to_ios(duplicate_io_names)
