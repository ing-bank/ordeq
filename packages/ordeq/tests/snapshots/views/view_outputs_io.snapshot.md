## Resource

```python
from ordeq import IO, node



@node(outputs=IO())
def view() -> str:
    return "Hello, World!"

```