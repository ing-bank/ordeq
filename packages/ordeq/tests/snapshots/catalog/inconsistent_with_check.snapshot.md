## Resource

```python
from ordeq import node
from ordeq._catalog import check_catalogs_are_consistent

from resources.catalog.catalogs import inconsistent, local

check_catalogs_are_consistent(local, inconsistent)
catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Exception

```text
CatalogError: Catalogs are inconsistent.
```

## Typing

```text
packages/ordeq/tests/resources/catalog/inconsistent_with_check.py:10: error: Module has no attribute "result"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```