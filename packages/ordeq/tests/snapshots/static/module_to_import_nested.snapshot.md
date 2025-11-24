## Resource

```python
import example_nested
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(example_nested))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))

```

## Output

```text
example_nested {}
example_nested.__main__ {'run': 'ordeq', 'world_relative': 'example_nested.subpackage.subsubpackage.hello_relative'}
example_nested.catalog {'StringBuffer': 'ordeq_common'}
example_nested.subpackage {}
example_nested.subpackage.subsubpackage {}
example_nested.subpackage.subsubpackage.hello {'node': 'ordeq', 'run': 'ordeq'}
example_nested.subpackage.subsubpackage.hello_relative {'node': 'ordeq', 'message': 'example_nested.catalog'}

```