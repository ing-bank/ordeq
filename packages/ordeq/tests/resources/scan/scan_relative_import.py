
import example_imports.relative_import
from ordeq._scan import scan

print("Should raise an error:")
_ = scan(example_imports.relative_import)
