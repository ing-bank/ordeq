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

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hooks.py", line LINO, in <module>
    run(func1, func2, hooks=[RunTimer()])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```