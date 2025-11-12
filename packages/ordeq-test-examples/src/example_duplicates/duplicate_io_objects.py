from copy import copy

from ordeq import IO

x = IO[str]()
y = x  # duplicate of 'x' by reference
z = copy(x)  # duplicate of 'x' by value
