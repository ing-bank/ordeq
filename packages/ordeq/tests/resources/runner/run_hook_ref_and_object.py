from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node '{node}'")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node '{node}'")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])
