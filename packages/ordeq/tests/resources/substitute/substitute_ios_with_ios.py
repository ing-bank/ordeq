from ordeq._substitute import _build_substitution_map

from ordeq import IO
from ordeq_common import StringBuffer

a = StringBuffer("a")
b = IO()
A = StringBuffer("A")
B = IO()

print(_build_substitution_map({a: A, b: B}))
