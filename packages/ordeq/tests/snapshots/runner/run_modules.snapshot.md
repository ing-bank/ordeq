## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Output

```text
Node:resources.runner.example_module_a:decrement --> io-1
Node:resources.runner.example_module_a:increment --> io-2
io-2 --> Node:resources.runner.example_module_a:decrement
Node:resources.runner.example_module_b:decrement --> io-3
Node:resources.runner.example_module_b:increment --> io-4
io-4 --> Node:resources.runner.example_module_b:decrement

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)

```

## Typing

```text
error[unresolved-import]: Cannot resolve imported module `resources.runner`
 --> packages/ordeq/tests/resources/runner/run_modules.py:2:6
  |
1 | from ordeq import run
2 | from resources.runner import example_module_a, example_module_b
  |      ^^^^^^^^^^^^^^^^
3 |
4 | run(example_module_a, example_module_b, verbose=True)
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