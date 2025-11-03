## Resource

```python
from example_catalogs import local_package
from ordeq._substitute import _substitutes_modules_to_ios

# Should return an empty map
print(_substitutes_modules_to_ios({local_package: local_package}))

```

## Output

```text
{}

```
