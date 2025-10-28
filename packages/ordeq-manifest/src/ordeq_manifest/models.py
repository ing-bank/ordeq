"""Ordeq project data models"""

import operator
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
    def from_io(cls, name: FQN, io: AnyIO) -> "IOModel":
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
        cls, name: FQN, node: Node, ios_to_id: dict[AnyIO, str]
    ) -> "NodeModel":
        return cls(
            id=fqn_to_str(name),
            name=name[1],
            inputs=[ios_to_id[i] for i in node.inputs],  # type: ignore[index,arg-type]
            outputs=[ios_to_id[o] for o in node.outputs],
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
            fqn_to_str(name): IOModel.from_io(name, io)
            for name, io in sorted(ios.items(), key=operator.itemgetter(0))
        }
        ios_to_id = {
            io: io_model.id
            for name, io in ios.items()
            if (io_model := io_models.get(fqn_to_str(name)))
        }
        node_models = {
            node.name: NodeModel.from_node(
                str_to_fqn(node.name), node, ios_to_id
            )
            for node in sorted(nodes_, key=lambda obj: obj.name)
        }
        return cls(name=name, nodes=node_models, ios=io_models)
