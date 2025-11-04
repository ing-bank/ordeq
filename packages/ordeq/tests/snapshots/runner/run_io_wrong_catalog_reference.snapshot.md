## Resource

```python
# Checks the behaviour when running nodes with a reference to an alternative
# catalog. We want to support this syntax and behaviour since it allows users
# to switch between catalogs without having to import the catalog.
from example_catalogs import local
from ordeq import node, run

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


# NOK: IO references need to be formatted 'module.submodule.[...]'
run(uppercase, io={catalog.hello: "example_catalogs:remote"})

```

## Exception

```text
ValueError: IO 'remote' not found in module 'example_catalogs'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_string_to_io
    raise ValueError(f"IO '{io_name}' not found in module '{module_name}'")

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in resolve_string_to_sub
    return _resolve_string_to_io(string)

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    new_sub = resolve_string_to_sub(new) if isinstance(new, str) else new
              ~~~~~~~~~~~~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/runner/run_io_wrong_catalog_reference.py", line LINO, in <module>
    run(uppercase, io={catalog.hello: "example_catalogs:remote"})
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```