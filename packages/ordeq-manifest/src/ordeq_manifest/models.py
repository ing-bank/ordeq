"""Ordeq project data models"""

import operator
from collections import defaultdict
from itertools import chain
from typing import Any

from ordeq import Node, View
from ordeq._fqn import FQN, fqn_to_str, str_to_fqn  # noqa: PLC2701
from ordeq._resolve import AnyIO, Catalog
from pydantic import BaseModel, Field


# TODO: explore storing nodes and edges instead
class IOModel(BaseModel):
    """Model representing an IO in a project."""

    name: str
    type: str
    references: dict[str, list[str]] = Field(default_factory=dict)

    @classmethod
    def from_io(cls, named_io: tuple[FQN, AnyIO], io_ids) -> "IOModel":
        name, io = named_io
        io_type = type(io)
        io_type_fqn = (io_type.__module__, io_type.__name__)
        return cls(
            name=name[1],
            type=fqn_to_str(io_type_fqn),
            references={
                attr: [io_ids[v] for v in vs]
                for attr, vs in io.references.items()
            }
            if hasattr(io, "references")
            else {},
        )


class NodeModel(BaseModel):
    """Model representing a node in a project."""

    name: str
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)
    view: bool

    @classmethod
    def from_node(
        cls, named_node: tuple[FQN, Node], io_ids: dict[AnyIO, list[str]]
    ) -> "NodeModel":
        name, node = named_node

        ins = []
        for i in node.inputs:  # type: ignore[index,arg-type]
            if isinstance(i, View):
                ins.append(i.name)
            else:
                ins.append(io_ids[i])

        return cls(
            name=name[1],
            inputs=ins,
            outputs=[io_ids[o] for o in node.outputs],  # type: ignore[index,arg-type]
            attributes=node.attributes,
            view=isinstance(node, View),
        )


class ModuleModel(BaseModel):
    """Model representing a module in a project."""

    name: str
    nodes: dict[str, str] = Field(default_factory=dict)
    ios: dict[str, str] = Field(default_factory=dict)


class ProjectModel(BaseModel):
    """Model representing a project."""

    name: str
    modules: list[ModuleModel] = Field(default_factory=list)
    nodes: dict[str, NodeModel] = Field(default_factory=dict)
    ios: dict[str, IOModel] = Field(default_factory=dict)

    @classmethod
    def from_nodes_and_ios(
        cls, name: str, nodes: set[Node], ios: Catalog
    ) -> "ProjectModel":
        """Create a ProjectModel from nodes and ios dictionaries.

        Args:
            name: The name of the project.
            nodes: A dictionary of NodeModel instances.
            ios: A dictionary of IOModel instances.

        Returns:
            A ProjectModel instance.
        """

        # Assign unique IDs to all IOs
        io_ids = {}
        c = 0
        for _, named_io in sorted(ios.items(), key=operator.itemgetter(0)):
            for _, io in sorted(named_io.items(), key=operator.itemgetter(0)):
                if io not in io_ids:
                    io_ids[io] = f"io-{c}"
                    c += 1

                if hasattr(io, "references"):
                    for vs in io.references.values():
                        for v in vs:
                            if v not in io_ids:
                                io_ids[v] = f"io-{c}"
                                c += 1
        for node in sorted(nodes, key=lambda obj: obj.name):
            for io in chain(node.inputs, node.outputs):
                if io not in io_ids:
                    io_ids[io] = f"io-{c}"
                    c += 1
                if hasattr(io, "references"):
                    for vs in io.references.values():
                        for v in vs:
                            if v not in io_ids:
                                io_ids[v] = f"io-{c}"
                                c += 1

        io_models = {
            io_ids[io]: IOModel.from_io(
                ((module_name, object_name), io), io_ids
            )
            for module_name, named_io in sorted(
                ios.items(), key=operator.itemgetter(0)
            )
            for object_name, io in named_io.items()
        }

        # All references to IOs by their IDs
        ios_to_id = defaultdict(list)
        for named_io in ios.values():
            for io in named_io.values():
                if io_models.get(io_ids[io]):
                    ios_to_id[io].append(io_ids[io])  # type: ignore[index]

        # Anonymous IOs
        idx = 0
        named_nodes = dict(
            sorted(
                {str_to_fqn(node.name): node for node in nodes}.items(),
                key=operator.itemgetter(0),
            )
        )
        an = defaultdict(dict)
        for (mod, _), node in named_nodes.items():
            for obj in chain(node.inputs, node.outputs):
                if obj not in ios_to_id:
                    # same module as node
                    ios_to_id[obj].append(f"{mod}:<anonymous{idx}>")  # type: ignore[index]
                    model = IOModel.from_io(
                        ((mod, f"<anonymous{idx}>"), obj), io_ids
                    )  # type: ignore[arg-type]
                    io_models[io_ids[obj]] = model
                    idx += 1
                    an[mod][f"<anonymous{idx}>"] = io_ids[obj]

        modules = []
        for module_name, iod in sorted(
            ios.items(), key=operator.itemgetter(0)
        ):
            ios = {name: io_ids[io] for name, io in iod.items()}
            ios.update(an.get(module_name, {}))
            modules.append(
                ModuleModel(
                    name=module_name,
                    nodes={
                        str_to_fqn(node.name)[1]: node.name
                        for node in sorted(nodes, key=lambda node: node.name)
                        if str_to_fqn(node.name)[0] == module_name
                    },
                    ios=ios,
                )
            )

        # Sort dictionaries by key for consistency
        io_models = dict(sorted(io_models.items(), key=operator.itemgetter(0)))

        node_models = {
            node.name: NodeModel.from_node(
                (str_to_fqn(node.name), node), io_ids
            )
            for node in sorted(nodes, key=lambda obj: obj.name)
        }

        return cls(
            name=name, modules=modules, nodes=node_models, ios=io_models
        )
