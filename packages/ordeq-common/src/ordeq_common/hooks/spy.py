from ordeq.hook import InputHook, NodeHook, OutputHook


class SpyHook(InputHook, OutputHook, NodeHook):
    """Hook that stores the arguments it is called with in a list. Typically
    only used for test purposes."""

    def __init__(self):
        self.called_with: list[tuple] = []

    def before_node_run(self, *args) -> None:
        return self._register_call("before_node_run", *args)

    def before_input_load(self, *args) -> None:
        return self._register_call("before_input_load", *args)

    def after_input_load(self, *args) -> None:
        return self._register_call("after_input_load", *args)

    def on_node_call_error(self, *args) -> None:
        return self._register_call("on_node_call_error", *args)

    def before_output_save(self, *args) -> None:
        return self._register_call("before_output_save", *args)

    def after_output_save(self, *args) -> None:
        return self._register_call("after_output_save", *args)

    def after_node_run(self, *args) -> None:
        return self._register_call("after_node_run", *args)

    def _register_call(self, item, *args) -> None:
        self.called_with.append((item, *args))
