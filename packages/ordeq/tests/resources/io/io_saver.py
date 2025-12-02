from ordeq_common import StringBuffer
from typing_extensions import reveal_type

s = StringBuffer("Hello, World!")

reveal_type(s._saver)
print(s._saver("~/.',.`#"))
print(s.load())
