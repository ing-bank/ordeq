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

## Exception

```text
TypeError: RunTimer.after_run() missing 1 required positional argument: 'data'
  File "/packages/ordeq/src/ordeq/_runner.py", line 180, in run
    run_hook.after_run(graph)
    ~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hooks.py", line 33, in <module>
    run(func1, func2, hooks=[RunTimer()])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
INFO	ordeq.runner	Running node "func2" in module "run_hooks"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "func1" in module "run_hooks"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```