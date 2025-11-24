## Resource

```python
import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(example_project))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))

```

## Output

```text
example_project {}
example_project.catalog_1 {'Input': 'ordeq', 'Print': 'ordeq_common', 'StringBuffer': 'ordeq_common'}
example_project.catalog_2 {'Input': 'ordeq', 'Print': 'ordeq_common', 'StringBuffer': 'ordeq_common'}
example_project.inner {}
example_project.inner.nodes {'IO': 'ordeq', 'node': 'ordeq', 'Print': 'ordeq_common'}
example_project.misc {}
example_project.nodes {'IO': 'ordeq', 'node': 'ordeq', 'Print': 'ordeq_common'}
example_project.nodes_import {'node': 'ordeq', 'a': 'example_project.catalog_1', 'b': 'example_project.catalog_1', 'f': 'example_project.catalog_2', 'catalog_1': 'example_project', 'catalog_2': 'example_project'}
example_project.nodes_import_alias {'node': 'ordeq', 'a': 'example_project.catalog_1', 'B': 'example_project.catalog_1', 'h': 'example_project.catalog_2'}
example_project.nodes_with_inline_io {'IO': 'ordeq', 'Input': 'ordeq', 'node': 'ordeq'}
example_project.nodes_with_view {'Input': 'ordeq', 'node': 'ordeq', 'Print': 'ordeq_common'}

```