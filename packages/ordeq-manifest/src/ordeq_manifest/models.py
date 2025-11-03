"""Ordeq project data models"""

import operator
from collections import defaultdict
from typing import Any, Self, TypeVar

from ordeq import Node, View
from ordeq._fqn import FQN, fqn_to_str, str_to_fqn  # noqa: PLC2701
from ordeq._resolve import AnyIO, Catalog
from pydantic import BaseModel, Field, model_validator

T = TypeVar("T")


def _sort_dict_items(d: dict[Any, T]) -> list[tuple[Any, T]]:
    return sorted(d.items(), key=operator.itemgetter(0))


def _generate_io_ids(nodes: set[Node], ios: Catalog) -> dict[AnyIO, str]:
    """Search for all IOs in nodes and catalog and assign unique IDs."""  # noqa: DOC201
    io_ids = {}
    counter = 0

    def register_io(io: AnyIO) -> None:
        nonlocal counter

        if io not in io_ids:
            io_ids[io] = f"io-{counter}"
            counter += 1
            if hasattr(io, "references"):
                for vs in io.references.values():
                    for v in vs:
                        register_io(v)

    # Register IOs from catalog
    for _, named_io in _sort_dict_items(ios):
        for _, io in _sort_dict_items(named_io):
            register_io(io)

    # Register IOs from nodes
    for node in sorted(nodes, key=lambda n: n.name):
        # Handle inputs and outputs separately due to different types
        for io in node.inputs:
            register_io(io)
        for io in node.outputs:
            register_io(io)

    return io_ids


class IOModel(BaseModel):
    """Model representing an IO in a project."""

    name: str
    type: str
    references: dict[str, list[str]] = Field(default_factory=dict)

    @classmethod
    def from_io(
        cls, named_io: tuple[FQN, AnyIO], io_ids: dict[AnyIO, str]
    ) -> "IOModel":
        name, io = named_io
        io_type = type(io)
        io_type_fqn = (io_type.__module__, io_type.__name__)

        references = {}
        # TODO: IOs should not be views in the first place
        if not isinstance(io, View):
            references = {
                attr: [io_ids[v] for v in vs]
                for attr, vs in io.references.items()
            }

        return cls(
            name=name[1], type=fqn_to_str(io_type_fqn), references=references
        )


class NodeModel(BaseModel):
    """Model representing a node in a project."""

    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)
    view: bool

    @classmethod
    def from_node(
        cls, named_node: tuple[FQN, Node], io_ids: dict[AnyIO, str]
    ) -> "NodeModel":
        node = named_node[1]

        inputs = [
            # TODO: handle view by replacing with anonymous IO ID
            i.name if isinstance(i, View) else io_ids[i]
            for i in node.inputs
        ]

        return cls(
            inputs=inputs,
            outputs=[io_ids[o] for o in node.outputs],
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

    @model_validator(mode="after")
    def check_ids_exist(self) -> Self:
        for module in self.modules:
            for node_name in module.nodes.values():
                if node_name not in self.nodes:
                    raise ValueError(
                        f"Node '{node_name}' in module '{module.name}' "
                        "not found in project nodes."
                    )
            for io_name in module.ios.values():
                if io_name not in self.ios:
                    raise ValueError(
                        f"IO '{io_name}' in module '{module.name}' "
                        "not found in project IOs."
                    )
        for nodes in self.nodes.values():
            for idx in nodes.inputs + nodes.outputs:
                if idx not in self.ios and idx not in self.nodes:
                    raise ValueError(
                        f"IO '{idx}' in node not found in project IOs "
                        f"or Nodes."
                    )

        for ios in self.ios.values():
            for refs in ios.references.values():
                for ref in refs:
                    if ref not in self.ios:
                        raise ValueError(
                            f"Referenced IO '{ref}' in IO '{ios.name}' "
                            "not found in project IOs."
                        )
        return self

    @classmethod
    def from_nodes_and_ios(
        cls, name: str, nodes: set[Node], ios: Catalog
    ) -> "ProjectModel":
        """Create a ProjectModel from nodes and ios dictionaries.

        Args:
            name: The name of the project
            nodes: A set of Node instances
            ios: A catalog of named IOs

        Returns:
            A ProjectModel instance
        """
        # Generate unique IDs for all IOs
        io_ids = _generate_io_ids(nodes, ios)

        # Create IO models
        io_models = {
            io_ids[io]: IOModel.from_io(
                ((module_name, object_name), io), io_ids
            )
            for module_name, named_io in _sort_dict_items(ios)
            for object_name, io in named_io.items()
            if not isinstance(io, View)
        }

        # Track references to IOs by their IDs
        ios_to_id = defaultdict(list)
        for named_io in ios.values():
            for io in named_io.values():
                if io_models.get(io_ids[io]):
                    ios_to_id[io].append(io_ids[io])

        # TODO: the reference keys are missing!

        # Handle anonymous IOs
        idx = 0
        anonymous_ios = defaultdict(dict)
        named_nodes = {str_to_fqn(node.name): node for node in nodes}

        for (module_name, _), node in _sort_dict_items(named_nodes):
            # Handle inputs and outputs separately
            for obj in node.inputs:
                if obj not in ios_to_id:
                    anonymous_name = f"<anonymous{idx}>"
                    ios_to_id[obj].append(f"{module_name}:{anonymous_name}")
                    io_models[io_ids[obj]] = IOModel.from_io(
                        ((module_name, anonymous_name), obj), io_ids
                    )
                    anonymous_ios[module_name][anonymous_name] = io_ids[obj]
                    idx += 1

            for obj in node.outputs:
                if obj not in ios_to_id:
                    anonymous_name = f"<anonymous{idx}>"
                    ios_to_id[obj].append(f"{module_name}:{anonymous_name}")
                    io_models[io_ids[obj]] = IOModel.from_io(
                        ((module_name, anonymous_name), obj), io_ids
                    )
                    anonymous_ios[module_name][anonymous_name] = io_ids[obj]
                    idx += 1

        # Create modules
        modules = []
        for module_name, module_ios in _sort_dict_items(ios):
            ios_dict = {name: io_ids[io] for name, io in module_ios.items()}
            ios_dict.update(anonymous_ios.get(module_name, {}))

            module_nodes = {
                str_to_fqn(node.name)[1]: node.name
                for node in sorted(nodes, key=lambda n: n.name)
                if str_to_fqn(node.name)[0] == module_name
            }

            modules.append(
                ModuleModel(name=module_name, nodes=module_nodes, ios=ios_dict)
            )

        # Create node models
        node_models = {
            node.name: NodeModel.from_node(
                (str_to_fqn(node.name), node), io_ids
            )
            for node in sorted(nodes, key=lambda n: n.name)
        }

        return cls(
            name=name,
            modules=modules,
            nodes=node_models,
            ios=dict(_sort_dict_items(io_models)),
        )
