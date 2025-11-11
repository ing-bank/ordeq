## Resource

```python
from ordeq import run

run("example_1", hooks=["example_1.hooks:other_obj"])

```

## Exception

```text
ValueError: Hook 'other_obj' not found in module 'example_1.hooks'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_ref_to_hook
    raise ValueError(
        f"Hook '{hook_name}' not found in module '{module_ref}'"
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_hooks
    resolved_hook = _resolve_ref_to_hook(hook)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    run_hooks, node_hooks = _resolve_hooks(*hooks)
                            ~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hook_ref_not_a_hook.py", line LINO, in <module>
    run("example_1", hooks=["example_1.hooks:other_obj"])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```