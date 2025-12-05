## Resource

```python
from ordeq import IO, Input, Output, node
from ordeq._runner import run

I1 = Input[str]()
I2 = Input[str]()
O1 = IO[str]()
O2 = Output[str]()


@node(inputs=[I1, I2], outputs=O1)
def f(i: str, j: str) -> str:
    return f"{i} {j}"


@node(inputs=O1, outputs=O2)
def g(a: str) -> str:
    return f(a, a)


run(f, g, verbose=True)  # raises NotImplementedError

```

## Output

```text
io-0 --> Node:__main__:f
io-1 --> Node:__main__:f
Node:__main__:f --> io-2
io-2 --> Node:__main__:g
Node:__main__:g --> io-3
IOException: Failed to load Input 'f:i' in module '__main__'.

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __call__
    return self.io.load()
           ~~~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_loader
    return io._loader()
           ~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _load_inputs
    data = _run_loader(io)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    args = _load_inputs(node.inputs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(
    ~~~~~~~~~~^
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/runner/incremental_placeholder.py", line LINO, in <module>
    run(f, g, verbose=True)  # raises NotImplementedError
    ~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.runner	Loading Input 'f:i' in module '__main__'

```