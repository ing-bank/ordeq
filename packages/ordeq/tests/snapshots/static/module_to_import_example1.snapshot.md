## Resource

```python
import example_1
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(example_1))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))

```

## Output

```text
example_1 {}
example_1.catalog {'Input': 'ordeq', 'Output': 'ordeq', 'StringBuffer': 'ordeq_common'}
example_1.hooks {'RunHook': 'ordeq'}
example_1.nodes {'node': 'ordeq', 'StringBuffer': 'ordeq_common'}
example_1.pipeline {'node': 'ordeq', 'World': 'example_1.catalog', 'Hello': 'example_1.catalog', 'TestInput': 'example_1.catalog', 'TestOutput': 'example_1.catalog'}
example_1.wrapped_io {'dataclass': 'dataclasses', 'IO': 'ordeq', 'Input': 'ordeq', 'Output': 'ordeq', 'node': 'ordeq', 'run': 'ordeq'}

```