from ordeq._nodes import _create_node


def func():
    ...


node = _create_node(func, inputs=[], outputs=[])
print('Original:', node)

node_renamed = _create_node(func, name="custom-name", inputs=[], outputs=[])
print('Renamed:', node_renamed)
