## Resource

```python
from ordeq import run

run(
    "packages.example",
    hooks=["packages.example.hooks:other_obj"]
)

```

## Exception

```text
ValueError: Hook 'other_obj' not found in module 'packages.example.hooks'
```