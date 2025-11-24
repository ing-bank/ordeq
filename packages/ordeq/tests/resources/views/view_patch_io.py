from ordeq import Input, node, run

hello_io = Input("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


run(n, verbose=True, io={hello_io: Input("Buenos dias")})
