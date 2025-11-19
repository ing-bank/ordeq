
import example_imports.execute_reassign
from ordeq._scan import scan

print("Should raise an error:")
_ = scan(example_imports.execute_reassign)
