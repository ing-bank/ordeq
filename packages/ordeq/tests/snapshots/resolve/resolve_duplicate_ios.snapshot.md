## Resource

```python
# Captures the behaviour when resolving a module containing the same names
# for the same IO.
from pprint import pprint

from example_duplicates import duplicate_io_name
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(duplicate_io_name)
pprint(ios)

```

## Output

```text
[('example_duplicates.duplicate_io_name',
  'x',
  Input(idx=ID1))]

```