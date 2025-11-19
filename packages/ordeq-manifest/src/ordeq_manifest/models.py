"""Ordeq project data models"""

from collections import defaultdict
from itertools import chain
from typing import Any

from ordeq import Node
from ordeq._fqn import FQ, fqn_to_object_ref
from ordeq._resolve import AnyIO, Catalog
from pydantic import BaseModel, Field


class ResourceModel(BaseModel):
    """Model representing a resource of an IO."""

    id: int
    type: str
    value: Any

    @classmethod
    def from_resource(cls, resource: Any, idx: int) -> "ResourceModel":
        resource_type = type(resource)
        return cls(
            id=idx,
            type=fqn_to_object_ref((
                resource_type.__module__,
                resource_type.__name__,
            )),
            value=resource,
        )


class IOModel(BaseModel):
    """Model representing an IO in a project."""

    name: str
    type: str
    resource: int | None = None
    references: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_io(cls, io: FQ[AnyIO], resource: int | None) -> "IOModel":
        (_, io_name), io_obj = io
        io_type = type(io_obj)
        io_type_fqn = (io_type.__module__, io_type.__name__)
        return cls(
            name=io_name,
            type=fqn_to_object_ref(io_type_fqn),
            references=list(io_obj.references.keys()),
            attributes=io_obj._attributes or {},
            resource=resource,
        )


class NodeModel(BaseModel):
    """Model representing a node in a project."""

    name: str
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_node(
        cls, node: FQ[Node], io_to_fqns: dict[AnyIO, list[str]]
    ) -> "NodeModel":
        (module_ref, node_name), node_obj = node
        ins = []
        for i in node_obj.inputs:
            candidates = io_to_fqns[i]
            if len(candidates) == 1:
                ins.append(candidates[0])
            else:
                candidates = [
                    c.removeprefix(module_ref + ":")
                    for c in candidates
                    if c.startswith(module_ref + ":")
                ]
                if len(candidates) == 1:
                    ins.append(module_ref + ":" + candidates[0])
                else:
                    ins.append(module_ref + ":" + "|".join(candidates))
        outs = []
        for o in node_obj.outputs:
            candidates = io_to_fqns[o]
            if len(candidates) == 1:
                outs.append(candidates[0])
            else:
                candidates = [
                    c.removeprefix(module_ref + ":")
                    for c in candidates
                    if c.startswith(module_ref + ":")
                ]
                if len(candidates) == 1:
                    outs.append(module_ref + ":" + candidates[0])
                else:
                    outs.append(module_ref + ":" + "|".join(candidates))

        return cls(
            name=node_name,
            inputs=ins,  # type: ignore[index,arg-type]
            outputs=outs,
            attributes=node_obj.attributes,
        )


class ProjectModel(BaseModel):
    """Model representing a project."""

    name: str
    nodes: dict[str, NodeModel] = Field(default_factory=dict)
    ios: dict[str, IOModel] = Field(default_factory=dict)
    resources: list[ResourceModel] = Field(default_factory=list)

    @classmethod
    def from_nodes_and_ios(
        cls, name: str, nodes: list[FQ[Node]], ios: Catalog
    ) -> "ProjectModel":
        """Create a ProjectModel from nodes and ios dictionaries.

        Args:
            name: The name of the project.
            nodes: A dictionary of NodeModel instances.
            ios: A dictionary of IOModel instances.

        Returns:
            A ProjectModel instance.
        """

        ref_to_io_models = {}
        io_to_fqns = defaultdict(list)
        resource_to_model: dict[Any, ResourceModel] = {}
        for module_ref in ios:
            for io_name, io in ios[module_ref].items():
                resource = io._resource
                if resource not in resource_to_model and resource is not io:
                    resource_to_model[resource] = ResourceModel.from_resource(
                        resource, idx=len(resource_to_model)
                    )
                ref = fqn_to_object_ref((module_ref, io_name))
                ref_to_io_models[ref] = IOModel.from_io(
                    ((module_ref, io_name), io),
                    resource_to_model[resource].id
                    if resource in resource_to_model
                    else None,
                )
                io_to_fqns[io].append(ref)

        # Anonymous IOs:
        # TODO: assign these names in a named graph in `ordeq`.
        idx = 0
        for (module_ref, _), node in nodes:
            for io_ in chain(node.inputs, node.outputs):
                if io_ not in io_to_fqns:
                    resource = io_._resource
                    if (
                        resource not in resource_to_model
                        and resource is not io_
                    ):
                        resource_to_model[resource] = (
                            ResourceModel.from_resource(
                                resource, idx=len(resource_to_model)
                            )
                        )
                    # same module as node
                    fqn = f"{module_ref}:<anonymous{idx}>"
                    io_to_fqns[io_].append(f"{module_ref}:<anonymous{idx}>")  # type: ignore[index]
                    model = IOModel.from_io(
                        ((module_ref, f"<anonymous{idx}>"), io_),  # type: ignore[arg-type]
                        resource_to_model[resource].id
                        if resource in resource_to_model
                        else None,
                    )  # type: ignore[arg-type]
                    ref_to_io_models[fqn] = model
                    idx += 1

        refs_to_nodes = {
            fqn_to_object_ref(fqn): NodeModel.from_node(
                (fqn, node), io_to_fqns
            )
            for fqn, node in nodes
        }
        return cls(
            name=name,
            nodes=refs_to_nodes,
            ios=ref_to_io_models,
            resources=list(resource_to_model.values()),
        )
