from ordeq._nodes import create_node


def func():
    ...


node = create_node(func, inputs=[], outputs=[])
print('Original:', node)

node_renamed = create_node(func, name="custom-name", inputs=[], outputs=[])
print('Renamed:', node_renamed)
