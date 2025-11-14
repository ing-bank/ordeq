from ordeq_common import Literal, Print, StringBuffer

d = Literal("a")
e = StringBuffer("b")

# Multiple nodes cannot share the same output
# For testing of the imports, we create separate Print instances
# In a real project, each node would have its own Print() in the
# @node decorator
f = Print()
g = Print()
h = Print()
i = Print()
j = Print()
