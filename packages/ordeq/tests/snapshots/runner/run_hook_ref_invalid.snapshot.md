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
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_hook_reference
    raise ValueError(f"Invalid hook reference: '{ref}'.")

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_hooks
    resolved_hook = _resolve_hook_reference(hook)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    run_hooks, node_hooks = _resolve_hooks(*hooks)
                            ~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hook_ref_invalid.py", line LINO, in <module>
    run(
    ~~~^
        "packages.example",
        ^^^^^^^^^^^^^^^^^^^
        hooks=["invalid"]
        ^^^^^^^^^^^^^^^^^
    )
    ^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```