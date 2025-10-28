"""Ordeq project data models"""

import operator
from collections import defaultdict
from itertools import chain
from typing import Any

from ordeq import Node, View
from ordeq._fqn import FQN, fqn_to_str, str_to_fqn  # noqa: PLC2701
from ordeq._resolve import AnyIO, Catalog
from pydantic import BaseModel, Field


class IOModel(BaseModel):
    """Model representing an IO in a project."""

    id: str
    name: str
    type: str
    references: list[str] = Field(default_factory=list)

    @classmethod
    def from_io(cls, named_io: tuple[FQN, AnyIO]) -> "IOModel":
        name, io = named_io
        io_type = type(io)
        io_type_fqn = (io_type.__module__, io_type.__name__)
        return cls(
            id=fqn_to_str(name),
            name=name[1],
            type=fqn_to_str(io_type_fqn),
            references=list(io.references.keys()),
        )


class NodeModel(BaseModel):
    """Model representing a node in a project."""

    id: str
    name: str
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_node(
        cls, named_node: tuple[FQN, Node], ios_to_id: dict[AnyIO, list[str]]
    ) -> "NodeModel":
        name, node = named_node
        ins = []
        for i in node.inputs:
            candidates = sorted(ios_to_id[i])  # type: ignore[index]
            if len(candidates) == 1:
                ins.append(candidates[0])
            else:
                candidates = [
                    c.removeprefix(name[0] + ":")
                    for c in candidates
                    if c.startswith(name[0] + ":")
                ]
                if len(candidates) == 1:
                    ins.append(name[0] + ":" + candidates[0])
                else:
                    ins.append(name[0] + ":" + "|".join(candidates))
        outs = []
        for o in node.outputs:
            candidates = sorted(ios_to_id[o])
            if len(candidates) == 1:
                outs.append(candidates[0])
            else:
                candidates = [
                    c.removeprefix(name[0] + ":")
                    for c in candidates
                    if c.startswith(name[0] + ":")
                ]
                if len(candidates) == 1:
                    outs.append(name[0] + ":" + candidates[0])
                else:
                    outs.append(name[0] + ":" + "|".join(candidates))

        return cls(
            id=fqn_to_str(name),
            name=name[1],
            inputs=ins,  # type: ignore[index,arg-type]
            outputs=outs,
            attributes=node.attributes,
        )


class ProjectModel(BaseModel):
    """Model representing a project."""

    name: str
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

        # Manifests don't accurately display views yet, so we filter them out
        nodes_ = [node for node in nodes if not isinstance(node, View)]

        io_models = {
            io_model.id: io_model
            for io_model in [
                IOModel.from_io(named_io)
                for named_io in sorted(ios.items(), key=operator.itemgetter(0))
            ]
        }

        # All references to IOs by their IDs
        ios_to_id = defaultdict(list)
        for io_name, io in ios.items():
            if io_model := io_models.get(fqn_to_str(io_name)):
                ios_to_id[io].append(io_model.id)

        # Anonymous IOs
        idx = 0
        named_nodes = dict(
            sorted(
                {str_to_fqn(node.name): node for node in nodes}.items(),
                key=operator.itemgetter(0),
            )
        )
        for (mod, _), node in named_nodes.items():
            for obj in chain(node.inputs, node.outputs):
                if obj not in ios_to_id:
                    # same module as node
                    ios_to_id[obj].append(f"{mod}:<anonymous{idx}>")  # type: ignore[index]
                    model = IOModel.from_io(((mod, f"<anonymous{idx}>"), obj))  # type: ignore[arg-type]
                    io_models[model.id] = model
                    idx += 1

        # Sort dictionaries by key for consistency
        io_models = dict(sorted(io_models.items(), key=operator.itemgetter(0)))
        ios_to_id = dict(sorted(ios_to_id.items(), key=operator.itemgetter(1)))  # type: ignore[assignment]

        node_models = {
            node_model.id: node_model
            for node_model in [
                NodeModel.from_node((str_to_fqn(node.name), node), ios_to_id)
                for node in sorted(nodes_, key=lambda obj: obj.name)
            ]
        }
        return cls(name=name, nodes=node_models, ios=io_models)
