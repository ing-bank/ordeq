from pprint import pprint

import example_2
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_2))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)
