from pprint import pprint

import example_rag_pipeline
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_rag_pipeline)
print("Nodes:")
pprint(
    sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40
)
print("IOs:")
pprint(list(ios.values()), width=40)
