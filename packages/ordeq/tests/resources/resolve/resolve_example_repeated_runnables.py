from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

import importlib

runnables = [
    importlib.import_module("example"),
    importlib.import_module("example"),
    importlib.import_module("example"),
    importlib.import_module("example.wrapped_io"),
    importlib.import_module("example.nodes"),
]


modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(dict(sorted(nodes.items())))
print(dict(sorted(ios.items())))

print(dict(sorted(_resolve_runnables_to_nodes(*runnables).items())))
