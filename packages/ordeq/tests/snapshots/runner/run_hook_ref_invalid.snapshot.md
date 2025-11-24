## Resource

```python
from ordeq import run

run("example_1", hooks=["invalid"])

```

## Output

```text
ValueError: Invalid object reference: 'invalid'. Expected format 'module:name'.
  File "/packages/ordeq/src/ordeq/_fqn.py", line LINO, in object_ref_to_fqn
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_fqn.py", line LINO, in from_ref
    fqn = object_ref_to_fqn(ref)

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_hook_refs
    fqn = FQN.from_ref(hook)

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_refs_to_hooks
    resolved_hooks = _resolve_hook_refs(*hooks)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    run_hooks, node_hooks = _resolve_refs_to_hooks(*hooks)
                            ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hook_ref_invalid.py", line LINO, in <module>
    run("example_1", hooks=["invalid"])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```