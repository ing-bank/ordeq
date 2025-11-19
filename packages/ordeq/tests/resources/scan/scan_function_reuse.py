from pprint import pprint

import example_function_reuse
from ordeq._scan import scan

nodes, ios = scan(example_function_reuse)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
