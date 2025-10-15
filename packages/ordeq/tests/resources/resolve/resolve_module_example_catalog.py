from example import catalog as mod  # ty: ignore[unresolved-import]

from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(mod)
print(ios)
