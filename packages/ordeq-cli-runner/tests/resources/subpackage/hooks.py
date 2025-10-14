from ordeq import RunHook, NodeHook


class _MyNodeHook(NodeHook):
    def before_node_run(self, *args, **kwargs) -> None:
        print("(before-node)")

    def after_node_run(self, *args, **kwargs) -> None:
        print("(after-node)")


class MyRunHook(RunHook):
    def before_run(self, *args, **kwargs) -> None:
        print("(before-run)")

    def after_run(self, *args, **kwargs) -> None:
        print("(after-run)")


MyNodeHook = _MyNodeHook()
MyRunHook = MyRunHook()
