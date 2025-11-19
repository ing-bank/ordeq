from collections import defaultdict
from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQ, FQN, ModuleRef, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import Node, _is_node, get_node
from ordeq._resolve import _resolve_packages_to_modules

RootType = ModuleRef | ModuleType

NodeToFQNs: TypeAlias = dict[Node, list[FQN]]
IOToFQNs: TypeAlias = dict[IOIdentity, list[FQ[AnyIO]]]


def scan(root: ModuleType) -> tuple[NodeToFQNs, IOToFQNs]:
    modules = _resolve_packages_to_modules(root)
    nodes: dict[Node, list[FQN]] = defaultdict(list)
    ios: dict[IOIdentity, list[FQ[AnyIO]]] = defaultdict(list)
    for module in sorted(modules, key=lambda m: m.__name__):
        for name, obj in vars(module).items():
            if _is_io(obj):
                io_id = id(obj)
                if io_id in ios:
                    fqn, _ = ios[io_id][0]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        # TODO: Trace the line where the aliasing happened
                        #  for more descriptive error message.
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                ios[io_id].append(((module.__name__, name), obj))
            elif _is_node(obj):
                node = get_node(obj)
                nodes[node].append((module.__name__, name))
    return dict(nodes), dict(ios)
