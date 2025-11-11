## Resource

```python
from pprint import pprint

from example_1 import catalog as mod
from ordeq._resolve import _resolve_module_to_ios

ios = _resolve_module_to_ios(mod)
pprint(ios)

```

## Output

```text
[('example_1.catalog',
  'Hello',
  StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 ('example_1.catalog',
  'World',
  StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
 ('example_1.catalog',
  'TestInput',
  Input(idx=ID1)),
 ('example_1.catalog',
  'TestOutput',
  Output(idx=ID2))]

```