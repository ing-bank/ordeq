## Resource

```python
from ordeq import node, run
from ordeq_common import Print, StringBuffer

io = StringBuffer("a")


@node(outputs=io)
def add_suffix() -> str:
    return "suffix"


@node(inputs=io, outputs=Print())
def print_value(val: str):
    return val


# This resource shows that IOs that are loaded after being outputted only
# load the data computed by the node, not the full data.
run(add_suffix, print_value)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_append.py", line LINO, in <module>
    run(add_suffix, print_value)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```