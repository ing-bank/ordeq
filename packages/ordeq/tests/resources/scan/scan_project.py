from pprint import pprint

import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_project))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
