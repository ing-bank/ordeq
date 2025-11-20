import example_imports.runtime_import
from ordeq._scan import scan

print("Should raise an error:")
_ = scan(example_imports.runtime_import)
