import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _ast_to_imports, _module_path_to_ast, _module_to_path

submodules = list(_resolve_packages_to_modules(example_function_reuse))
for submodule in submodules:
    imports = _ast_to_imports(
        _module_path_to_ast(_module_to_path(submodule)),
        module_name=submodule.__name__,
        relevant_modules={
            "example_function_reuse.catalog": {"A", "B"},
            "example_function_reuse.func_defs": {"print_input"},
        },
    )
    if imports:
        print(submodule.__name__, imports)
