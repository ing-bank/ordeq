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