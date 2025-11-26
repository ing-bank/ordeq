import example_imports.execute_reassign
from ordeq._scan import _scan_fqns

print("Should raise an error:")
_ = _scan_fqns(example_imports.execute_reassign)
