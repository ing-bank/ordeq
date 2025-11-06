## Resource

```python
from ordeq import node, run
from resources.runner import example_module_a


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)

```

## Output

```text
Node:resources.runner.example_module_a:decrement --> io-1
Node:resources.runner.example_module_a:increment --> io-2
io-2 --> Node:resources.runner.example_module_a:decrement
View:run_module_and_node:noop --> io-3

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_module_and_node:noop'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "noop" in module "run_module_and_node"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```

## Typing

```text
error[unresolved-import]: Cannot resolve imported module `resources.runner`
 --> packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6
  |
1 | from ordeq import node, run
2 | from resources.runner import example_module_a
  |      ^^^^^^^^^^^^^^^^
  |
info: Searched in the following paths during module resolution:
info:   1.  (first-party code)
info:   2. vendored://stdlib (stdlib typeshed stubs vendored by ty)
info:   3. /.venv/lib/python3.13/site-packages (site-packages)
info:   4. /examples/integration-streamlit/src (editable install)
info:   5. /packages/ordeq/src (editable install)
info:   ... and 38 more paths. Run with `-v` to see all paths.
info: make sure your Python environment is properly configured: https://docs.astral.sh/ty/modules/#python-environment
info: rule `unresolved-import` is enabled by default

Found 1 diagnostic

```