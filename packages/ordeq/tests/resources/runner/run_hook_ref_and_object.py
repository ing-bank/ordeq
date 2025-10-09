from ordeq import run
from ordeq import NodeHook


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node: {node.name}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node: {node.name}")


run(
    "packages.example",
    hooks=["packages.example.hooks:MyHook", MyHook()]
)
