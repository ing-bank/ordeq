## Resource

```python
from example_catalogs import remote_extended
from ordeq import node, run

catalog = remote_extended


@node(inputs=catalog.hello, outputs=catalog.another_io)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)  # 'catalog.another_io' prints the output to stdout

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

  File "/packages/ordeq/tests/resources/catalog/overriden.py", line LINO, in <module>
    run(func1)  # 'catalog.another_io' prints the output to stdout
    ~~~^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```