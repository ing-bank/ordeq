import example_imports.runtime_import
from ordeq._index import index

print("Should raise an error:")
_ = index(example_imports.runtime_import)
