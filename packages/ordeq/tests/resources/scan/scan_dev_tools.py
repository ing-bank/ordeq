from pprint import pprint

import ordeq_dev_tools
from ordeq._scan import scan

nodes, ios = scan(ordeq_dev_tools)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
