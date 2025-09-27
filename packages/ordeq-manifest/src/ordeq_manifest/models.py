from typing import Any

from pydantic import BaseModel, Field


class IOModel(BaseModel):
    """Model representing an IO in a project.

    # TODO: Add hooks to the model.

    """

    id: str
    name: str
    type: str


class NodeModel(BaseModel):
    """Model representing a node in a project.

    # TODO: Add hooks to the model.

    """

    id: str
    name: str
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    tags: list[str] | dict[str, Any] = Field(default_factory=list)


class ProjectModel(BaseModel):
    """Model representing a project.

    # TODO: Add hooks to the model.

    """

    name: str
    nodes: dict[str, NodeModel] = Field(default_factory=dict)
    ios: dict[str, IOModel] = Field(default_factory=dict)
