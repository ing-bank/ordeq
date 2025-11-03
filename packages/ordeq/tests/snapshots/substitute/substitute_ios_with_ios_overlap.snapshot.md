## Resource

```python
from ordeq._substitute import _substitutes_modules_to_ios

from ordeq import IO
from ordeq_common import StringBuffer

a = StringBuffer("a")
b = IO()
A = StringBuffer("A")
B = IO()

print(_substitutes_modules_to_ios({a: A, b: b}))
print(_substitutes_modules_to_ios({a: A, b: a}))
print(_substitutes_modules_to_ios({a: A, A: a}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(idx=ID1): IO(idx=ID1)}
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(idx=ID1): StringBuffer(_buffer=<_io.StringIO object at HASH1>)}
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH2>): StringBuffer(_buffer=<_io.StringIO object at HASH1>)}

```
