## Resource

```python
import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _ast_to_imports, _module_path_to_ast, _module_to_path

submodules = list(_resolve_packages_to_modules(example_project))
for submodule in submodules:
    imports = _ast_to_imports(
        _module_path_to_ast(_module_to_path(submodule)),
        module_name=submodule.__name__,
        relevant_modules={
            "example_project.catalog_1": {"a", "b"},
            "example_project.catalog_2": {"h", "f"},
        },
    )
    if imports:
        print(submodule.__name__, imports)

```

## Output

```text
example_project.nodes_import {'a': 'example_project.catalog_1', 'b': 'example_project.catalog_1', 'f': 'example_project.catalog_2'}
example_project.nodes_import_alias {'a': 'example_project.catalog_1', 'b': 'example_project.catalog_1', 'h': 'example_project.catalog_2'}

```