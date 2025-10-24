## Resource

```python
from ordeq import node

from resources.catalog.catalogs import inconsistent

catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Exception

```text
AttributeError: module 'resources.catalog.catalogs.inconsistent' has no attribute 'result'
```

## Typing

```text
packages/ordeq/tests/resources/catalog/inconsistent_without_check.py:8: error: Module has no attribute "result"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```