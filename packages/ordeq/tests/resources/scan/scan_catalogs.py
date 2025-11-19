from pprint import pprint

import example_catalogs
from ordeq._scan import scan

nodes, ios = scan(example_catalogs)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
