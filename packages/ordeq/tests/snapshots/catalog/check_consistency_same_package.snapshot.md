## Resource

```python
from example_catalogs import package_base
from ordeq import check_catalogs_are_consistent

# Should pass without errors:
check_catalogs_are_consistent(package_base, package_base)

```

## Warnings

```text
RuntimeWarning: coroutine 'retrieve_data_1' was never awaited
```