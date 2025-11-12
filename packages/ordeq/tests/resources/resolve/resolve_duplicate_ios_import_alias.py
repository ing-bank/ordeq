# Captures the behaviour when resolving a module containing the same object
from example_duplicates import duplicate_import_alias
from ordeq._resolve import _resolve_module_to_ios

_ = _resolve_module_to_ios(duplicate_import_alias)
