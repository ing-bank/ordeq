from collections.abc import Callable
from unittest.mock import Mock

import pytest
from ordeq import Node
from ordeq.framework.hook import NodeHook
from ordeq_cli_runner.runner import get_hook, get_node, get_obj, get_pipeline
from ordeq_common import Static


@pytest.fixture(scope="module")
def node_1():
    return Mock(Node)


@pytest.fixture(scope="module")
def node_2():
    return Mock(Node)


@pytest.fixture(scope="module")
def node_3():
    return Mock(Node)


@pytest.fixture(scope="module")
def pipeline(node_1, node_2, node_3) -> set[Callable]:
    return {node_1, node_2, node_3}


@pytest.fixture(scope="module")
def module(node_1, node_2, node_3, pipeline) -> Mock:
    mock_module = Mock()
    mock_module.node_1 = node_1
    mock_module.node_2 = node_2
    mock_module.node_3 = node_3
    mock_module.pipeline = pipeline
    mock_module.something_else = "something_else"
    return mock_module


A, B, C, D, E, F = [Static(c) for c in "ABCDEF"]


class TestGetObj:
    def test_it_gets_an_obj(self, module: Mock, node_2: Node):
        assert get_obj("module:node_2", _get_module=lambda _: module) == node_2

    def test_it_gets_an_obj_with_double_colon_ref(
        self, module: Mock, node_2: Node
    ):
        # noinspection PyTypeChecker
        with pytest.raises(AttributeError):
            get_obj("module::node_2", _get_module=lambda _: object)


class TestGetNode:
    def test_it_gets_a_node(self, node_1: Node):
        assert get_node("module:node_1", _get_obj=lambda _: node_1) == node_1

    def test_it_raises_an_error_if_not_a_node(self, node_2: Node):
        with pytest.raises(
            TypeError, match="'module:something_else' is not a node"
        ):
            # noinspection PyTypeChecker
            get_node("module:something_else", _get_obj=lambda _: -1)


class TestGetPipeline:
    def test_it_gets_a_pipeline(self, pipeline: set[Callable]):
        assert (
            get_pipeline("module:pipeline", _get_obj=lambda _: pipeline)
            == pipeline
        )

    def test_it_raises_an_error_if_not_a_pipeline(
        self, pipeline: set[Callable]
    ):
        with pytest.raises(
            TypeError, match="'module:something_else' is not a pipeline"
        ):
            # noinspection PyTypeChecker
            get_pipeline("module:something_else", _get_obj=lambda _: "str")


class MyHook(NodeHook): ...


something = ""  # something that is not a hook


class TestGetHook:
    def test_it_gets_a_hook(self, pipeline: set[Callable]):
        assert get_hook(f"{__name__}:{MyHook.__name__}") == MyHook

    def test_it_raises_an_error_if_not_a_pipeline(
        self, pipeline: set[Callable]
    ):
        with pytest.raises(
            TypeError, match=f"'{__name__}:something' is not a hook"
        ):
            get_hook(f"{__name__}:something")
