from ordeq import IO, Input, node, run

placeholder = IO()

hello = Input("Hello")


@node(inputs=[Input("Jane"), hello], outputs=placeholder)
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


@node(inputs=placeholder)
def what_i_heard(v: str) -> None:
    print(f"I heard that {v}")


@node(inputs=what_i_heard)
def sink(s: str) -> None:
    print(s)


# This should succeed, as it produces the placeholder IO's value
run(hello_from_someone, sink, verbose=True)

# This should fail: it attempts to load placeholder IO
run(sink, verbose=True)
