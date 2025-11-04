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

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/runner/runner_load_output.py", line LINO, in <module>
    run(my_node, load_node)
    ~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'runner_load_output:load_node'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```