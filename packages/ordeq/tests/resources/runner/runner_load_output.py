from ordeq import Output, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"


@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)


run(my_node, load_node)
