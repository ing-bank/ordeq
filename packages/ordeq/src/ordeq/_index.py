from collections.abc import Callable
from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQ, FQN, ObjectRef, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import Node, _is_node, get_node
from ordeq._resolve import _resolve_packages_to_modules

NodeIndex: TypeAlias = dict[Node | FQN | Callable | ObjectRef, FQ[Node]]
IOIndex: TypeAlias = dict[IOIdentity | FQN | ObjectRef, FQ[AnyIO]]


def index(*modules: ModuleType) -> tuple[NodeIndex, IOIndex]:
    nodes: NodeIndex = {}
    ios: IOIndex = {}
    modules_ = _resolve_packages_to_modules(*modules)
    for module in modules_:
        for name, obj in vars(module).items():
            fqn = (module.__name__, name)
            ref = fqn_to_object_ref(fqn)
            fq_obj = (fqn, obj)
            if _is_io(obj):
                io_id = id(obj)
                if io_id in ios:
                    existing_fqn, _ = ios[io_id]
                    existing_ref = fqn_to_object_ref(existing_fqn)
                    if name != existing_fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                ios[io_id] = fq_obj
                ios[fqn] = fq_obj
                ios[ref] = fq_obj
            if _is_node(obj):
                if obj in nodes:
                    existing_fqn, _ = nodes[obj]
                    existing_ref = fqn_to_object_ref(existing_fqn)
                    if name != existing_fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases node "
                            f"'{existing_ref}' to '{name}'. "
                            f"Nodes cannot be aliased."
                        )
                node = get_node(obj)
                nodes[node] = fq_obj
                nodes[obj] = fq_obj
                nodes[fqn] = fq_obj
                nodes[ref] = fq_obj
    return nodes, ios
