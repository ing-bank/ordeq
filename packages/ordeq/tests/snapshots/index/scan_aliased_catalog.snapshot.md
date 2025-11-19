## Resource

```python
from pprint import pprint

import example_imports.aliased_catalog
from ordeq._index import index

nodes, ios = index(example_imports.aliased_catalog)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
{}
IOs:
{4424363344: (('example_imports.aliased_catalog',
               'a'),
              IO(id=ID1)),
 'example_imports.aliased_catalog:a': (('example_imports.aliased_catalog',
                                        'a'),
                                       IO(id=ID1)),
 ('example_imports.aliased_catalog', 'a'): (('example_imports.aliased_catalog',
                                             'a'),
                                            IO(id=ID1))}

```