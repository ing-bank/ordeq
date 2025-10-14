import pytest
from ordeq import IO, Node, node
from ordeq._nodes import get_node
from ordeq._runner import _run_node
from ordeq_common.io.string_buffer import StringBuffer


class TestNode:
    @pytest.mark.parametrize(
        ("kwargs", "expected"),
        [({"x": "_X_"}, "_X_ + Y"), ({"x": "_X_", "y": "_Y_"}, "_X_ + _Y_")],
    )
    def test_it_runs_with_defaulted_args(self, kwargs, expected):
        @node(inputs=StringBuffer("x"), outputs=StringBuffer("z"))
        def func(x: str, y: str = "Y") -> str:
            return f"{x} + {y}"

        actual = func(**kwargs)

        assert actual == expected

    @pytest.mark.parametrize(
        ("inputs", "expected"),
        [
            ((), ""),
            ((StringBuffer("a"),), "a"),
            ((StringBuffer("a"), StringBuffer("b")), "ab"),
        ],
    )
    def test_it_runs_with_args(self, inputs, expected):
        @node(inputs=inputs, outputs=StringBuffer("z"))
        def func(*args: str) -> str:
            return "".join(args)

        actual = func(*(i.load() for i in inputs))

        assert actual == expected


@pytest.mark.parametrize(
    "inputs",
    [
        (),  # too few
        (StringBuffer("a"), StringBuffer("b")),  # 1 too many
        (
            StringBuffer("a"),
            StringBuffer("b"),
            StringBuffer("c"),
        ),  # 2 too many
    ],
)
def test_it_raises_for_invalid_inputs(inputs: tuple[IO]):
    with pytest.raises(  # noqa: PT012
        ValueError, match="Node inputs invalid for function arguments"
    ):
        n = Node.from_func(
            func=lambda _: _, inputs=inputs, outputs=(StringBuffer("c"),)
        )
        _run_node(n, hooks=())


def method_w_0_ret(a: str) -> None:
    return


def method_w_1_ret(a: str) -> str:
    return a


def method_w_2_ret(a: str) -> tuple[str, str]:
    return a, a


@pytest.mark.parametrize(
    ("func", "outputs"),
    [
        (method_w_0_ret, (StringBuffer("a"), StringBuffer("b"))),  # 1 too many
        (
            method_w_0_ret,
            (StringBuffer("a"), StringBuffer("b"), StringBuffer("c")),
        ),  # 2 too many
        (method_w_1_ret, ()),  # too few
        (method_w_1_ret, (StringBuffer("a"), StringBuffer("b"))),  # 1 too many
        (
            method_w_1_ret,
            (StringBuffer("a"), StringBuffer("b"), StringBuffer("c")),
        ),  # 2 too many
        (method_w_2_ret, ()),  # too few
        (
            method_w_2_ret,
            (StringBuffer("a"), StringBuffer("b"), StringBuffer("c")),
        ),  # 1 too many
    ],
)
def test_it_raises_for_invalid_outputs(func, outputs: tuple[IO]):
    with pytest.raises(  # noqa: PT012
        ValueError, match="Node outputs invalid for return annotation"
    ):
        n = Node.from_func(
            func=func, inputs=(StringBuffer("a"),), outputs=outputs
        )
        _run_node(n, hooks=())


class TestGetNode:
    def test_it_gets_registered_node(self):
        @node(inputs=[StringBuffer("a")], outputs=[StringBuffer("b")])
        def my_func(a: str) -> str:
            return a

        node_obj = get_node(my_func)
        assert node_obj is not None
        assert node_obj.func == my_func

    def test_it_raises_node_not_found(self):
        def my_func(a: str) -> str:
            return a

        with pytest.raises(ValueError, match="'my_func' is not a node"):
            get_node(my_func)
