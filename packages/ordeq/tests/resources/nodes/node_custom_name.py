from ordeq import Node


def func():
    ...


node = Node.from_func(func, inputs=[], outputs=[])
print('Original:', node)

node_renamed = Node.from_func(func, name="custom-name", inputs=[], outputs=[])
print('Renamed:', node_renamed)
