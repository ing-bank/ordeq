import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _ast_to_imports, _module_path_to_ast, _module_to_path

submodules = list(_resolve_packages_to_modules(ordeq_dev_tools))
for submodule in submodules:
    imports = _ast_to_imports(
        _module_path_to_ast(_module_to_path(submodule)),
        module_name=submodule.__name__,
        relevant_modules={"ordeq_dev_tools.pipelines.shared": {"packages"}},
    )
    if imports:
        print(submodule.__name__, imports)
