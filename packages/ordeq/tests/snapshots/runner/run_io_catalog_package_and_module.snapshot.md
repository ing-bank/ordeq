## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import (
    local,
    local_package,
    remote_extended,
    remote_package,
)
from ordeq import node, run
from ordeq_common import Print

catalog = local_package


@node(inputs=local_package.hello, outputs=remote_extended.hello)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=remote_extended.another_io, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(
    uppercase,
    add_world,
    io={local_package: remote_package, remote_extended: local},
)

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.local' is missing IO(s) 'another_io'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    check_catalogs_are_consistent(old, new)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    substitution_map.update(_substitute(key, value))
                            ~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    substitution_map = _substitutes_modules_to_ios(io)

  File "/packages/ordeq/tests/resources/runner/run_io_catalog_package_and_module.py", line LINO, in <module>
    run(
    ~~~^
        uppercase,
        ^^^^^^^^^^
        add_world,
        ^^^^^^^^^^
        io={local_package: remote_package, remote_extended: local},
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```