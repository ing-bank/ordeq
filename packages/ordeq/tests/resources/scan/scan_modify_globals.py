
import example_imports.modify_globals
from ordeq._scan import scan

print("Should raise an error:")
_ = scan(example_imports.modify_globals)
