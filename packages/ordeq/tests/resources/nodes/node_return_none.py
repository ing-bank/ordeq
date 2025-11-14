from ordeq import IO, node, run

io = IO[None]()


@node(outputs=[io])
def node_return_none() -> None:
    print("This should run first")


@node(inputs=[io])
def node_consume_none(_data: None) -> None:
    print("This should run second")


if __name__ == "__main__":
    run(node_return_none, node_consume_none)
