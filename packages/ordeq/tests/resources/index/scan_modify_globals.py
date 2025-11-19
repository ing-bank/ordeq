import example_imports.modify_globals
from ordeq._index import index

print("Should raise an error:")
_ = index(example_imports.modify_globals)
