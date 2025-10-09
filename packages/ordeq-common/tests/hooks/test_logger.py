import logging

import pytest
from ordeq_common import LoggerHook


def test_it_logs(caplog: pytest.CaptureFixture):
    caplog.set_level(logging.INFO)
    spy = LoggerHook()
    spy.before_node_run("a", 1)
    spy.before_input_load("b")
    spy.after_input_load("c")
    spy.on_node_call_error("d", "error details")
    spy.before_output_save("e")
    spy.after_output_save()
    spy.after_node_run(None)
    assert caplog.record_tuples == [
        (
            "LoggerHook",
            logging.INFO,
            "Called 'before_node_run' with args: ('a', 1)",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'before_input_load' with args: ('b',)",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'after_input_load' with args: ('c',)",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'on_node_call_error' with args: ('d', 'error details')",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'before_output_save' with args: ('e',)",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'after_output_save' with args: ()",
        ),
        (
            "LoggerHook",
            logging.INFO,
            "Called 'after_node_run' with args: (None,)",
        ),
    ]
