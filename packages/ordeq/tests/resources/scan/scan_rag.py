from pprint import pprint

import example_rag_pipeline
from ordeq._scan import scan

nodes, ios = scan(example_rag_pipeline)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
