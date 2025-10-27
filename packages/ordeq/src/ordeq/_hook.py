from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Protocol,
    TypeAlias,
    TypeVar,
    runtime_checkable,
)

if TYPE_CHECKING:
    from ordeq._graph import NodeGraph
    from ordeq._io import AnyIO, Input, Output
    from ordeq._nodes import Node

T = TypeVar("T")


@runtime_checkable
class InputHook(Protocol[T]):
    """Hook used to inject custom logic that will be executed before and after
    an input is loaded."""

    def before_input_load(self, io: Input[T]) -> None:
        """Hook that is executed before an input is loaded.

        Args:
            io: the input object.
        """

        return

    def after_input_load(self, io: Input[T], data: T) -> None:
        """Hook that is executed after an input is loaded.

        Args:
            io: the input object.
            data: the loaded data.
        """

        return


@runtime_checkable
class OutputHook(Protocol[T]):
    """Hook used to inject custom logic that will be executed before and after
    an output is saved."""

    def before_output_save(self, io: Output[T], data: T) -> None:
        """Hook that is executed before an output is saved.

        Args:
            io: the input object.
            data: the data to be saved.
        """

        return

    def after_output_save(self, io: Output[T], data: T) -> None:
        """Hook that is executed after an output is saved.

        Args:
            io: the input object.
            data: the data that has been saved.
        """

        return


@runtime_checkable
class NodeHook(Protocol):
    """Hook used to inject custom logic that will be executed when a node is
    run."""

    def before_node_run(self, node: Node) -> None:
        return None

    def on_node_call_error(self, node: Node, error: Exception) -> None:
        """Triggered when an exception is raised when calling the node.

        Args:
            node: the node object
            error: the error
        """

        return

    def after_node_run(self, node: Node) -> None:
        return None


@runtime_checkable
class RunHook(Protocol):
    """Hook used to inject custom logic that will be executed when a graph is
    run."""

    def before_run(self, graph: NodeGraph) -> None:
        """Triggered before the graph is run.

        Args:
            graph: the graph object
        """

        return

    def after_run(self, graph: NodeGraph, data: dict[AnyIO, Any]) -> None:
        """Triggered after the graph is run.

        Args:
            graph: the graph object
            data: mapping of all inputs and outputs to their loaded/saved data
        """
        return


# Type aliases
RunnerHook: TypeAlias = RunHook | NodeHook
Hook: TypeAlias = InputHook | OutputHook | RunnerHook
