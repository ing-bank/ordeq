import ast
import importlib.util
from collections import defaultdict
from pathlib import Path
from types import ModuleType
from typing import TypeVar

from ordeq import Node
from ordeq._fqn import FQN
from ordeq._io import AnyIO

T = TypeVar("T", Node, AnyIO)


def _module_name_to_path(module_name: str) -> Path:
    spec = importlib.util.find_spec(module_name, None)
    if spec is None or spec.origin is None:
        raise ModuleNotFoundError(
            f"Cannot find module '{module_name}' or it has no origin."
        )
    return Path(spec.origin)


def _module_to_path(module: ModuleType) -> Path:
    module_path = module.__file__
    if module_path is None:
        raise FileNotFoundError(
            f"Module {module.__name__} has no __file__ attribute."
        )
    return Path(module_path)


def _module_path_to_ast(module_path: Path) -> ast.Module:
    source = Path(module_path).read_text(encoding="utf-8")
    return ast.parse(source, filename=module_path)


def _ast_to_imports(
    tree: ast.Module, module_name: str, relevant_modules: dict[str, set[str]]
) -> dict[str, str]:
    imports = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.level > 0:
                # handling of relative imports
                parent = module_name.rsplit(".", node.level)[0]
                module_name = (
                    parent
                    if node.module is None
                    else parent + f".{node.module}"
                )
            else:
                module_name = node.module or ""

            if module_name not in relevant_modules:
                continue

            for alias in node.names:
                if alias.name == "*":
                    # skip wildcard imports
                    continue

                name = alias.asname or alias.name
                if name not in relevant_modules[module_name]:
                    continue
                imports[name] = module_name
    return imports


def _select_canonical_fqn_using_imports(
    obj_fqns: dict[T, list[FQN]],
) -> dict[T, list[FQN]]:
    objects_with_multiple_fqns = []
    modules = set()
    relevant = defaultdict(set)

    for obj, fqns in obj_fqns.items():
        if len(fqns) > 1:
            for f in fqns:
                modules.add(f.module)
                relevant[f.module].add(f.name)
            objects_with_multiple_fqns.append(obj)

    removals: set[FQN] = set()
    for module in modules:
        module_path = _module_name_to_path(module)
        tree = _module_path_to_ast(module_path)
        imports = _ast_to_imports(tree, module, relevant)
        removals.update(FQN(module=module, name=name) for name in imports)

    for obj in objects_with_multiple_fqns:
        obj_fqns[obj] = [fqn for fqn in obj_fqns[obj] if fqn not in removals]
    return obj_fqns
