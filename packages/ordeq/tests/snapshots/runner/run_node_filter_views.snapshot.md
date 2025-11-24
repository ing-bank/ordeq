## Resource

```python
from ordeq import Input, Node, node, run
from ordeq_common import Print

greeting = Input("Hello")


@node(inputs=greeting, prints=False)
def hello(hi: str) -> str:
    return hi


@node(inputs=hello, outputs=Print(), prints=True)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def prints(n: Node) -> bool:
    return n.attributes.get("prints", False)


print("Should run both `hello` and `world`:")
# Even though the filter only returns True for `world`, `hello` is a view
# and is run because `world` is run.
run(hello, world, node_filter=prints, verbose=True)

print("Should run neither `hello` nor `world`:")
run(hello, node_filter=prints, verbose=True)

print("Should run both `hello` and `world`:")
run(world, node_filter=prints, verbose=True)

```

## Output

```text
Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
Saying Hello, world!!
Hello, world!!
Should run neither `hello` nor `world`:

Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
IOException: Failed to load Input(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _load_inputs
    data = cast("Input", input_dataset).load()

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    args = _load_inputs(node.inputs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_node_filter_views.py", line LINO, in <module>
    run(world, node_filter=prints, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running view 'hello' in module '__main__'
INFO	ordeq.runner	Running node 'world' in module '__main__'
INFO	ordeq.io	Saving Print()
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Input(id=ID1)

```