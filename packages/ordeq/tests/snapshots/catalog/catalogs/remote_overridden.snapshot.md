## Resource

```python
from ordeq import Input
from ordeq_common import Literal

# 'remote' is the catalog that is overridden
from resources.catalog.catalogs.remote import *  # noqa: F403 (import all definitions)

hello: Input[str] = Literal(
    "Hey I am overriding the hello IO"
)  # this overrides the base catalog

```

## Typing

```text
packages/ordeq/tests/resources/catalog/catalogs/remote_overridden.py:7: error: Name "hello" already defined (possibly by an import)  [no-redef]
Found 1 error in 1 file (checked 1 source file)

```