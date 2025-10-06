from ordeq import node, IO, run


O = IO[None]()


@node(outputs=[O])
def node_return_none() -> None:
    print("This should run first")


@node(inputs=[O])
def node_consume_none(_data: None) -> None:
    print("This should run second")


if __name__ == "__main__":
    run(node_return_none, node_consume_none)
