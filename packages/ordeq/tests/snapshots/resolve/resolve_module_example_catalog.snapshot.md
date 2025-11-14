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
{'Hello': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
 'TestInput': Input(idx=ID1),
 'TestOutput': Output(idx=ID2),
 'World': StringBuffer(_buffer=<_io.StringIO object at HASH2>)}

```