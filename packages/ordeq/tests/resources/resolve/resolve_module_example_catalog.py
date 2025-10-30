from example_1 import catalog as mod
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(mod)
print(ios)
