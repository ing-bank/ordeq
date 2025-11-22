import ast
from pathlib import Path
from types import ModuleType


def _module_to_ast(module: ModuleType) -> ast.Module:
    module_path = module.__file__
    if module_path is None:
        raise FileNotFoundError

    source = Path(module_path).read_text(encoding="utf-8")
    return ast.parse(source, filename=module_path)


def _module_to_imports(module: ModuleType) -> dict[str, str]:
    imports = {}
    tree = _module_to_ast(module)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.level > 0:
                # handling of relative imports
                parent = module.__name__.rsplit(".", node.level)[0]
                module_name = parent + f".{node.module}"
            else:
                module_name = node.module or ""

            for alias in node.names:
                if alias.name == "*":
                    # skip wildcard imports
                    continue
                imports[alias.asname or alias.name] = module_name
    return imports
