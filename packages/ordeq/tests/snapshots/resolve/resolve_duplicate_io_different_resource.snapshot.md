## Resource

```python
# Captures the behaviour when resolving a module containing the same names
# for the same IO.
from example_duplicates import duplicate_io_different_resource
from ordeq._resolve import _resolve_module_to_ios

_ = _resolve_module_to_ios(duplicate_io_different_resource)

```

## Logging

```text
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.

```