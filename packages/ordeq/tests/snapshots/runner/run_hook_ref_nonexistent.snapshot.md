## Resource

```python
from ordeq import run

run(
    "packages.example",
    hooks=["packages.example.hooks:idontexist"]
)

```

## Exception

```text
ValueError: Hook 'idontexist' not found in module 'packages.example.hooks'
```