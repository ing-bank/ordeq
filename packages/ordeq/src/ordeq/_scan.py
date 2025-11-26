from collections import defaultdict
from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQN
from ordeq._io import IOIdentity, _is_io
from ordeq._nodes import Node, _is_node

NodeFQNs: TypeAlias = dict[Node, list[FQN]]
IOFQNs: TypeAlias = dict[IOIdentity, list[FQN]]


def _scan_fqns(*modules: ModuleType) -> tuple[NodeFQNs, IOFQNs]:
    node_fqns: NodeFQNs = defaultdict(list)
    io_fqns: IOFQNs = defaultdict(list)
    for module in modules:
        for name, obj in vars(module).items():
            if _is_io(obj):
                io_id = id(obj)
                if io_id in io_fqns:
                    existing_fqn = io_fqns[io_id][0]
                    if name != existing_fqn.name:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_fqn.ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                io_fqns[io_id].append(FQN(module.__name__, name))
            elif _is_node(obj):
                if obj in node_fqns:
                    existing = node_fqns[obj][0]
                    if name != existing.name:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases node "
                            f"{existing} to '{name}'. "
                            f"Nodes cannot be aliased."
                        )
                node_fqns[obj].append(FQN(module.__name__, name))
    return dict(node_fqns), dict(io_fqns)
