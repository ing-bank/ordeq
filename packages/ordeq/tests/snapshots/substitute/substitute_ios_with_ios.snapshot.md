## Resource

```python
from ordeq._substitute import _build_substitution_map

from ordeq import IO
from ordeq_common import StringBuffer

a = StringBuffer("a")
b = IO()
A = StringBuffer("A")
B = IO()

# Should replace 'a' by 'A' and 'b' by 'B':
print(_build_substitution_map({a: A, b: B}))
# Should replace 'a' by 'A' and 'A' by 'a':
print(_build_substitution_map({a: A, A: a}))
# Should replace 'a' by 'A' and 'b' by 'a':
print(_build_substitution_map({a: A, b: a}))
# IOs are equal: don't include substitution map:
print(_build_substitution_map({a: a, b: b}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(idx=ID1): IO(idx=ID2)}
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH2>): StringBuffer(_buffer=<_io.StringIO object at HASH1>)}
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(idx=ID1): StringBuffer(_buffer=<_io.StringIO object at HASH1>)}
{}

```