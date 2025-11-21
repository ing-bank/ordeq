from collections.abc import Callable
from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQ, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import _is_node

NodeIndex: TypeAlias = dict[Callable, FQ[Callable]]
IOIndex: TypeAlias = dict[IOIdentity, FQ[AnyIO]]


def scan(*modules: ModuleType) -> tuple[NodeIndex, IOIndex]:
    node_index: NodeIndex = {}
    io_index: IOIndex = {}
    for module in modules:
        for name, obj in vars(module).items():
            if _is_io(obj):
                io_id = id(obj)
                if io_id in io_index:
                    fqn, _ = io_index[io_id]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                io_index[io_id] = (module.__name__, name), obj
            elif _is_node(obj):
                if obj in node_index:
                    fqn, _ = node_index[obj]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases node "
                            f"'{existing_ref}' to '{name}'. "
                            f"Nodes cannot be aliased."
                        )
                node_index[obj] = (module.__name__, name), obj
    return node_index, io_index
