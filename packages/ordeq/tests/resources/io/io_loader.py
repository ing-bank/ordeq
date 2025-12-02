from typing_extensions import reveal_type

from ordeq_common import StringBuffer

s = StringBuffer("Hello, World!")

reveal_type(s._loader)
print(s._loader)
print(s._loader())
