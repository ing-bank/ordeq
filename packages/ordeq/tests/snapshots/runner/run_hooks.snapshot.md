## Resource

```python
from time import time, sleep
from ordeq import RunHook
from ordeq import node, run
from ordeq_common import StringBuffer


class RunTimer(RunHook):
    start_time: float

    def before_run(self, graph):
        self.start_time = time()

    def after_run(self, graph, data):
        end_time = time()
        elapsed_time = end_time - self.start_time
        print(f"Total run time: {elapsed_time:.1f} seconds")


x = StringBuffer()
y = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


@node(outputs=y)
def func2() -> str:
    return "world"


run(func1, func2, hooks=[RunTimer()])

```

## Output

```text
Total run time: 0.0 seconds

```

## Logging

```text
INFO	ordeq.runner	Running node Node(name=run_hooks:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node Node(name=run_hooks:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```