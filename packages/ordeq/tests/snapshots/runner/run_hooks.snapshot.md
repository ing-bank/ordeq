## Resource

```python
from time import time

from ordeq import RunHook, node, run
from ordeq_common import StringBuffer


class RunTimer(RunHook):
    start_time: float

    def before_run(self, graph):
        self.start_time = time()

    def after_run(self, graph):
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
INFO	ordeq.runner	Running node "func2" in module "run_hooks"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "func1" in module "run_hooks"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```