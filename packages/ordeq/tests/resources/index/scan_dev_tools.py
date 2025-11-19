from pprint import pprint

import ordeq_dev_tools
from ordeq._index import index

nodes, ios = index(ordeq_dev_tools)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
