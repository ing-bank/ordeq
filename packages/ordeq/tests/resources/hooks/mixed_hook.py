from ordeq import Node, NodeHook, Output, OutputHook, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


class MixedHook(NodeHook, OutputHook):
    node: Node | None = None

    def before_node_run(self, node: Node):
        self.node = node

    def before_output_save(self, output: Output, data) -> None:
        if self.node is not None:
            print(
                f"Hook: before saving output of node {self.node.name} "
                f"with data: {data}"
            )


hook = MixedHook()
example = Example().with_output_hooks(hook)


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"


run(my_node, hooks=[hook])
