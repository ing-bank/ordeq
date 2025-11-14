from ordeq import node, run


@node
def world() -> None:
    print("Hello, World!")


if __name__ == "__main__":
    run(world)
