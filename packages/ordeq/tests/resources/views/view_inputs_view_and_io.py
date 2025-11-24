from ordeq import Input, node, run


@node
def hello() -> str:
    return "Hello, World!"


print(repr(hello))


@node(inputs=[Input("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(hello_from_someone))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


run(n, verbose=True)
