"""Ordeq project data models"""

import operator
from typing import Any

from ordeq import IO, Input, Node, Output
from pydantic import BaseModel, Field


class IOModel(BaseModel):
    """Model representing an IO in a project."""

    id: str
    name: str
    type: str
    references: list[str] = Field(default_factory=list)

    @classmethod
    def from_io(
        cls, name: tuple[str, str], io: IO | Input | Output
    ) -> "IOModel":
        idx = ".".join(name)
        t = type(io)
        return cls(
            id=idx,
            name=name[1],
            type=f"{t.__module__}.{t.__name__}",
            references=list(io.references.keys()),
        )


class NodeModel(BaseModel):
    """Model representing a node in a project."""

    id: str
    name: str
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    tags: list[str] | dict[str, Any] = Field(default_factory=list)

    @classmethod
    def from_node(
        cls,
        name: tuple[str, str],
        node: Node,
        ios_to_id: dict[IO | Input | Output, str],
    ) -> "NodeModel":
        return cls(
            id=".".join(name),
            name=name[1],
            inputs=[ios_to_id[i] for i in node.inputs],
            outputs=[ios_to_id[o] for o in node.outputs],
            tags=node.tags,
        )


class ProjectModel(BaseModel):
    """Model representing a project."""

    name: str
    nodes: dict[str, NodeModel] = Field(default_factory=dict)
    ios: dict[str, IOModel] = Field(default_factory=dict)

    @classmethod
    def from_nodes_and_ios(
        cls, name: str, nodes: set[Node], ios: dict[str, IO | Input | Output]
    ) -> "ProjectModel":
        """Create a ProjectModel from nodes and ios dictionaries.

        Args:
            name: The name of the project.
            nodes: A dictionary of NodeModel instances.
            ios: A dictionary of IOModel instances.

        Returns:
            A ProjectModel instance.
        """
        io_models = {
            name: IOModel.from_io(("ios", name), io)
            for name, io in sorted(ios.items(), key=operator.itemgetter(0))
        }
        ios_to_id = {
            io: io_model.id
            for name, io in ios.items()
            if (io_model := io_models.get(name))
        }
        node_models = {
            f"nodes.{node.name}": NodeModel.from_node(
                ("nodes", node.name), node, ios_to_id
            )
            for node in sorted(nodes, key=lambda obj: obj.name)
        }
        return cls(name=name, nodes=node_models, ios=io_models)
