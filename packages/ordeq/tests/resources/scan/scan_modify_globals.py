import example_imports.modify_globals
from ordeq._scan import _scan_fqns

print("Should raise an error:")
_ = _scan_fqns(example_imports.modify_globals)
