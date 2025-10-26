from collections.abc import Callable

from ordeq import node
from ordeq._nodes import get_node, create_node
from ordeq_common import StringBuffer

mock_x = StringBuffer("X")
mock_y = StringBuffer("Y")
mock_z = StringBuffer("Z")


@node(inputs=[mock_x], outputs=[mock_z])
def func(x: str = "X") -> Callable:
    @node(inputs=[mock_y], outputs=[mock_z])
    def inner(y: str) -> str:
        return x + y

    return inner


inner_func = func()
assert inner_func("X") == "XX"
assert get_node(func) == create_node(func=func, inputs=(mock_x,),
                                        outputs=(mock_z,))
assert get_node(inner_func) == create_node(
    func=inner_func, inputs=(mock_y,), outputs=(mock_z,)
)
