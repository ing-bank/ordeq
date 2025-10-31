## Resource

```python
from ordeq import run
from resources.runner.example_module_b import renamed

# The runner information shows name 'increment' for this node.
# That's the original name. We'd like to see 'renamed' instead.
# TODO: Add a method _resolve_proxy_to_node that gets the node,
# and sets its name to the proxy's name.
run(renamed, verbose=True)

```

## Output

```text
Node:resources.runner.example_module_b:increment --> io-1

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```

## Typing

```text
error[unresolved-import]: Cannot resolve imported module `resources.runner.example_module_b`
 --> packages/ordeq/tests/resources/runner/renamed_node.py:2:6
  |
1 | from ordeq import run
2 | from resources.runner.example_module_b import renamed
  |      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3 |
4 | # The runner information shows name 'increment' for this node.
  |
info: Searched in the following paths during module resolution:
info:   1.  (first-party code)
info:   2. vendored://stdlib (stdlib typeshed stubs vendored by ty)
info:   3. /.venv/lib/python3.13/site-packages (site-packages)
info:   4. /packages/ordeq/src (editable install)
info:   5. /packages/ordeq-altair/src (editable install)
info:   ... and 30 more paths. Run with `-v` to see all paths.
info: make sure your Python environment is properly configured: https://docs.astral.sh/ty/modules/#python-environment
info: rule `unresolved-import` is enabled by default

Found 1 diagnostic

```