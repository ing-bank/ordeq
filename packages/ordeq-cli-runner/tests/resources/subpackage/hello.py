from ordeq import node, NodeHook, RunHook


@node
def world() -> None:
    print("Hello, World!")
