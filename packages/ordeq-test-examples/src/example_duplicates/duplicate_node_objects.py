from copy import copy

from ordeq import node

x = node(lambda: None)
y = x  # duplicate of 'x' by reference
z = copy(x)  # duplicate of 'x' by value
