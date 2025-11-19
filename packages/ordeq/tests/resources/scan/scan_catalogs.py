from pprint import pprint

import example_catalogs
from ordeq._scan import scan

nodes, ios = scan(example_catalogs)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
