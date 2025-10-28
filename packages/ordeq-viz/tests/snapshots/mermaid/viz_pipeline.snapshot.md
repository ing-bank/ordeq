## Resource

```python
import example  # ty: ignore[unresolved-import]

from ordeq._resolve import _resolve_runnables_to_nodes_and_ios
from ordeq_viz import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, connect_wrapped_datasets=False)
print(diagram)

```

## Exception

```text
ImportError: cannot import name 'pipeline_to_mermaid' from 'ordeq_viz' (/packages/ordeq-viz/src/ordeq_viz/__init__.py)
  File "/packages/ordeq-viz/tests/resources/mermaid/viz_pipeline.py", line LINO, in <module>
    from ordeq_viz import pipeline_to_mermaid

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq-viz/tests/resources/mermaid/viz_pipeline.py:1: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/mermaid/viz_pipeline.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq-viz/tests/resources/mermaid/viz_pipeline.py:4: error: Module "ordeq_viz" has no attribute "pipeline_to_mermaid"  [attr-defined]
Found 2 errors in 1 file (checked 1 source file)

```