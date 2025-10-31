## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote, remote_overridden
from ordeq import node, run
from ordeq_common import Print, StringBuffer

catalog = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world,
    io={catalog: remote_overridden,
        catalog.result: StringBuffer("I want to say: ")})

```

## Exception

```text
AttributeError: 'StringBuffer' object has no attribute '__name__'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_package_to_ios
    modules = _resolve_packages_to_modules([(package.__name__, package)])
                                             ^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    sorted(_resolve_package_to_ios(old).items()),
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    substitution_map = _build_substitution_map(io)

  File "/packages/ordeq/tests/resources/runner/run_io_catalog_package_and_io.py", line LINO, in <module>
    run(uppercase, add_world,
    ~~~^^^^^^^^^^^^^^^^^^^^^^
        io={catalog: remote_overridden,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            catalog.result: StringBuffer("I want to say: ")})
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```