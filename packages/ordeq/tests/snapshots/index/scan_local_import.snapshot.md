## Resource

```python
from pprint import pprint

import example_imports.local_import
from ordeq._index import index

nodes, ios = index(example_imports.local_import)
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
{4424363344: (('example_imports.local_import',
               'a'),
              IO(id=ID1)),
 'example_imports.local_import:a': (('example_imports.local_import',
                                     'a'),
                                    IO(id=ID1)),
 ('example_imports.local_import', 'a'): (('example_imports.local_import',
                                          'a'),
                                         IO(id=ID1))}

```