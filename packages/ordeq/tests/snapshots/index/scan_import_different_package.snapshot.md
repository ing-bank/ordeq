## Resource

```python
from pprint import pprint

import example_imports.import_different_package
from ordeq._index import index

nodes, ios = index(example_imports.import_different_package)
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
{4414693024: (('example_imports.import_different_package',
               'Hello'),
              StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 'example_imports.import_different_package:Hello': (('example_imports.import_different_package',
                                                     'Hello'),
                                                    StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 ('example_imports.import_different_package', 'Hello'): (('example_imports.import_different_package',
                                                          'Hello'),
                                                         StringBuffer(_buffer=<_io.StringIO object at HASH1>))}

```