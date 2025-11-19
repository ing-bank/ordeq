## Resource

```python
from ordeq import Output, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"


@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)


run(my_node, load_node)

```

## Output

```text
saving! Hello, World!
AttributeError: 'Example' object has no attribute 'load'
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    data = cast("Input", input_dataset).load()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/runner_load_output.py", line LINO, in <module>
    run(my_node, load_node)
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
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:load_node'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "my_node" in module "__main__"
INFO	ordeq.io	Saving Output(id=ID1)

```