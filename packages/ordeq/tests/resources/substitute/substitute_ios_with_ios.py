from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios
from ordeq_common import StringBuffer

a = StringBuffer("a")
b = IO()
A = StringBuffer("A")
B = IO()

# Should replace 'a' by 'A' and 'b' by 'B':
print(_substitutes_modules_to_ios({a: A, b: B}))
# Should replace 'a' by 'A' and 'A' by 'a':
print(_substitutes_modules_to_ios({a: A, A: a}))
# Should replace 'a' by 'A' and 'b' by 'a':
print(_substitutes_modules_to_ios({a: A, b: a}))
# IOs are equal: don't include substitution map:
print(_substitutes_modules_to_ios({a: a, b: b}))
