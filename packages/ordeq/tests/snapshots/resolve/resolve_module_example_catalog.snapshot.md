## Resource

```python
from example import catalog as mod  # ty: ignore[unresolved-import]

from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(mod)
print(ios)

```

## Output

```text
{('example.catalog', 'Hello'): StringBuffer(_buffer=<_io.StringIO object at HASH1>), ('example.catalog', 'World'): StringBuffer(_buffer=<_io.StringIO object at HASH2>), ('example.catalog', 'TestInput'): Input(idx=ID1), ('example.catalog', 'TestOutput'): Output(idx=ID2)}

```

## Typing

```text
packages/ordeq/tests/resources/resolve/resolve_module_example_catalog.py:1: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/resolve/resolve_module_example_catalog.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```