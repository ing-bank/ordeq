import example_imports.relative_import
from ordeq._index import index

print("Should raise an error:")
_ = index(example_imports.relative_import)
