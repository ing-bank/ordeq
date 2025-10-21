from dataclasses import dataclass
from io import StringIO
from typing import Any

from ordeq import IO, node
from ordeq._nodes import get_node
from ordeq_spark import SparkJobGroupHook


@dataclass(frozen=True)
class MockIO(IO):
    # Mock IO that, upon load, returns a static value defined on init.

    load_value: Any | None = None
    buffer: StringIO | None = None

    def load(self) -> Any | None:
        return self.load_value

    def save(self, data: Any) -> None:
        if self.buffer is not None:
            self.buffer.write(data)


def test_spark_hook(spark):
    @node(inputs=[], outputs=[MockIO("x")])
    def hello() -> str:
        return "world"

    hook = SparkJobGroupHook()
    hook.before_node_run(get_node(hello))
