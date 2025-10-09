from logging import Logger, getLogger

from ordeq.hook import InputHook, NodeHook, OutputHook

_DEFAULT_LOGGER = getLogger("LoggerHook")


class LoggerHook(InputHook, OutputHook, NodeHook):
    """Hook that prints the calls to the methods.
    Typically only used for test purposes."""

    def __init__(self, logger: Logger = _DEFAULT_LOGGER):
        self._logger = logger

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
        self._logger.info("Called '%s' with args: %s", item, args)
