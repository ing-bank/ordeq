## Resource

```python
from pprint import pprint

import example_imports.local_import_made_global
from ordeq._index import index

nodes, ios = index(example_imports.local_import_made_global)
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
{4424363344: (('example_imports.local_import_made_global',
               'a'),
              IO(id=ID1)),
 'example_imports.local_import_made_global:a': (('example_imports.local_import_made_global',
                                                 'a'),
                                                IO(id=ID1)),
 ('example_imports.local_import_made_global', 'a'): (('example_imports.local_import_made_global',
                                                      'a'),
                                                     IO(id=ID1))}

```