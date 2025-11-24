from ordeq import IO, Input, node


@node(inputs=Input("Buenos dias"), outputs=IO())
def greet(hello: str):
    print(hello)
