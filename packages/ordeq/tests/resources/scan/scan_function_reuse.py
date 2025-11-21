from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)
