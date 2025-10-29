## Resource

```python
# Checks the behaviour when running an identity node with IO that has a
# read-write lock of some sorts. We expect this to raise an error when
# saving to the locked IO (not when building the graph).
from tempfile import NamedTemporaryFile

from ordeq import node, run, IO
from pathlib import Path


class File(IO):
    def __init__(self, p: Path):
        self.path = p
        super().__init__()

    def save(self, value: str) -> None:
        if self.lock:
            raise RuntimeError("Cannot write to a locked file.")
        self.path.write_text(value)

    def load(self) -> str:
        self.lock = True  # Simulate a read-write lock
        return self.path.read_text()


with NamedTemporaryFile(mode='wt') as tmp:
    path = Path(tmp.name)
    tmp.write("Hello, Ordeq!")
    tmp.flush()
    file = File(path)


    @node(inputs=file, outputs=file)
    def identity(value: str) -> str:
        return value


    run(identity, verbose=True)

```

## Exception

```text
IOException: Failed to save IO(idx=ID1).
Cannot write to a locked file.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **kwargs)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    composed(data, *args, **kwargs)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _save_outputs
    output_dataset.save(data)
    ~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    computed = _save_outputs(node, values, save=save)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/runner/identity_node_rw_lock.py", line LINO, in <module>
    run(identity, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     identity_node_rw_lock:identity -> []
  Nodes:
     identity_node_rw_lock:identity: Node(name=identity_node_rw_lock:identity, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID1)])

```

## Logging

```text
INFO	ordeq.io	Loading IO(idx=ID1)
INFO	ordeq.runner	Running node "identity" in module "identity_node_rw_lock"
INFO	ordeq.io	Saving IO(idx=ID1)

```