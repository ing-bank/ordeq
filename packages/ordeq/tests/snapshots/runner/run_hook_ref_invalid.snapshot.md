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
ValueError: Invalid hook reference: 'invalid'.
  File "/packages/ordeq/src/ordeq/_resolve.py", line 162, in _resolve_hook_reference
    raise ValueError(f"Invalid hook reference: '{ref}'.")

  File "/packages/ordeq/src/ordeq/_resolve.py", line 194, in _resolve_hooks
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

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```