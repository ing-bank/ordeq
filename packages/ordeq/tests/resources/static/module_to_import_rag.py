import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(example_rag_pipeline))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))
