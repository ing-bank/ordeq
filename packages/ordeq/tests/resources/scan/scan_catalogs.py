from pprint import pprint

import example_catalogs
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_catalogs))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
