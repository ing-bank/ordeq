from ordeq._fqn import FQN
from ordeq_common import StringBuffer
from typing_extensions import reveal_type

s = StringBuffer("Hello, World!")

reveal_type(s._saver)
print(s._saver)
s._saver("~/.',.`#")
print(s.load())
s._set_fqn(FQN(__name__, "s"))
print(s._saver)
