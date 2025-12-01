## Resource

```python
import example_nested
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _ast_to_imports, _module_path_to_ast, _module_to_path

submodules = list(_resolve_packages_to_modules(example_nested))
for submodule in submodules:
    imports = _ast_to_imports(
        _module_path_to_ast(_module_to_path(submodule)),
        module_name=submodule.__name__,
        relevant_modules={
            "example_nested.subpackage.subsubpackage.hello_relative": {
                "world_relative"
            }
        },
    )
    if imports:
        print(submodule.__name__, imports)

```

## Output

```text
example_nested.__main__ {'world_relative': 'example_nested.subpackage.subsubpackage.hello_relative'}

```