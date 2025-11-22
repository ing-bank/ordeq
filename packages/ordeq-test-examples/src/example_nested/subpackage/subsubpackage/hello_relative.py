from ordeq import node

from ...catalog import message


@node(outputs=message)
def world_relative() -> str:
    message = "Relativistic mass"
    print(message)
    return message
