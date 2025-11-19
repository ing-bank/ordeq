from pprint import pprint

import example_function_reuse
from ordeq._scan import scan

nodes, ios = scan(example_function_reuse)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
