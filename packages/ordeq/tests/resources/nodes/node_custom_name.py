from ordeq import Node


def func():
    ...


node = Node.create(func, inputs=[], outputs=[])
print('Original:', node)

node_renamed = Node.create(func, name="custom-name", inputs=[], outputs=[])
print('Renamed:', node_renamed)
