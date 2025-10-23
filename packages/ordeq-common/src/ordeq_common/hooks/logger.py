import logging
from logging import Logger, getLogger

from ordeq import InputHook, NodeHook, OutputHook

_DEFAULT_LOGGER = getLogger("LoggerHook")
_DEFAULT_LOGGER.setLevel(logging.INFO)


class LoggerHook(InputHook, OutputHook, NodeHook):
    """Hook that prints the calls to the methods.
    Typically only used for test purposes."""

    def __init__(
        self, *, logger: Logger = _DEFAULT_LOGGER, level: int | None = None
    ) -> None:
        self._logger = logger
        self._level = logger.level
        if level is not None:
            self._level = level

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
        self._logger.log(self._level, "Called '%s' with args: %s", item, args)
