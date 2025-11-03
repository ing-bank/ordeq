## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote_package

# Should return an empty map
print(_build_substitution_map({local: local}))

```

## Output

```text
{}

```