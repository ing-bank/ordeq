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


# NOK: IO references need to be formatted 'module:name'
run(uppercase, io={catalog.hello: "example_catalogs.remote.hello"})

```

## Output

```text
ModuleNotFoundError: No module named 'example_catalogs.remote.hello'; 'example_catalogs.remote' is not a package
  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load_unlocked

  File "<frozen importlib._bootstrap>", line LINO, in _find_and_load

  File "<frozen importlib._bootstrap>", line LINO, in _gcd_import

  File "/importlib/__init__.py", line LINO, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_ref_to_module
    return importlib.import_module(module_ref)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in resolve_ref_to_sub
    return _resolve_module_ref_to_module(ref)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _resolve_refs_to_subs
    new_sub = resolve_ref_to_sub(new) if isinstance(new, str) else new
              ~~~~~~~~~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    resolved_subs = _resolve_refs_to_subs(io or {})

  File "/packages/ordeq/tests/resources/runner/run_io_wrong_io_reference.py", line LINO, in <module>
    run(uppercase, io={catalog.hello: "example_catalogs.remote.hello"})
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```