from typing_extensions import reveal_type

from ordeq_common import StringBuffer

io = StringBuffer("Hello!")
print(reveal_type(io.load))
print(io.load)
print(io.load())
