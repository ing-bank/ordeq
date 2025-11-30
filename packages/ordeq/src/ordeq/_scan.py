from collections import defaultdict
from types import ModuleType
from typing import TypeAlias

from ordeq._fqn import FQN
from ordeq._io import AnyIO, _is_io
from ordeq._nodes import Node, _is_node

NodeFQNs: TypeAlias = dict[Node, list[FQN]]
IOFQNs: TypeAlias = dict[AnyIO, list[FQN]]


def _scan_fqns(*modules: ModuleType) -> tuple[NodeFQNs, IOFQNs]:
    node_fqns: NodeFQNs = defaultdict(list)
    io_fqns: IOFQNs = defaultdict(list)
    for module in modules:
        for name, obj in vars(module).items():
            if _is_io(obj):
                if obj in io_fqns:
                    existing_fqn = io_fqns[obj][0]
                    if name != existing_fqn.name:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_fqn.ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                fqn = FQN(module.__name__, name)
                if fqn not in io_fqns[obj]:
                    io_fqns[obj].append(fqn)
            elif _is_node(obj):
                if obj in node_fqns:
                    existing = node_fqns[obj][0]
                    if name != existing.name:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases node "
                            f"{existing} to '{name}'. "
                            f"Nodes cannot be aliased."
                        )
                fqn = FQN(module.__name__, name)
                if fqn not in node_fqns[obj]:
                    node_fqns[obj].append(fqn)
    return dict(node_fqns), dict(io_fqns)
