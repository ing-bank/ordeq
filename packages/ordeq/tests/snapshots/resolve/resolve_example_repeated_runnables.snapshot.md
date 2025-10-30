## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_1"),
    importlib.import_module("example_1"),
    importlib.import_module("example_1"),
    importlib.import_module("example_1.wrapped_io"),
    importlib.import_module("example_1.example.nodes"),
]


modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Exception

```text
ModuleNotFoundError: No module named 'example_1.example'
  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load_unlocked

  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load

  File "<frozen importlib._bootstrap>", line LINO, in _gcd_import

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load_unlocked

  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load

  File "<frozen importlib._bootstrap>", line LINO, in _gcd_import

  File "/importlib/__init__.py", line LINO, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/resolve/resolve_example_repeated_runnables.py", line LINO, in <module>
    importlib.import_module("example_1.example.nodes"),
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```