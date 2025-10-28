## Resource

```python
from ordeq import run

run(
    "packages.example",
    hooks=["invalid"]
)

```

## Exception

```text
ValueError: Invalid object reference: 'invalid'. Expected format 'module:name'.
  File "/packages/ordeq/src/ordeq/_fqn.py", line 28, in str_to_fqn
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line 161, in _resolve_hook_reference
    module_name, hook_name = str_to_fqn(ref)
                             ~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_resolve.py", line 192, in _resolve_hooks
    resolved_hook = _resolve_hook_reference(hook)

  File "/packages/ordeq/src/ordeq/_runner.py", line 183, in run
    run_hooks, node_hooks = _resolve_hooks(*hooks)
                            ~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hook_ref_invalid.py", line 3, in <module>
    run(
    ~~~^
        "packages.example",
        ^^^^^^^^^^^^^^^^^^^
        hooks=["invalid"]
        ^^^^^^^^^^^^^^^^^
    )
    ^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```