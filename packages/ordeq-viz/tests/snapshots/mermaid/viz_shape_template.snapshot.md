## Resource

```python

from ordeq._nodes import get_node
from ordeq_viz import pipeline_to_mermaid

from example import nodes as mod  # ty: ignore[unresolved-import]

diagram = pipeline_to_mermaid(
    nodes={("example", "world"): get_node(mod.world)},
    ios={("...", "x"): mod.x, ("...", "y"): mod.y},
    io_shape_template="(/"{value}/")",
    node_shape_template="(/"{value}/")",
)
print(diagram)

```

## Exception

```text
ImportError: cannot import name 'pipeline_to_mermaid' from 'ordeq_viz' (/packages/ordeq-viz/src/ordeq_viz/__init__.py)
  File "/packages/ordeq-viz/tests/resources/mermaid/viz_shape_template.py", line LINO, in <module>
    from ordeq_viz import pipeline_to_mermaid

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq-viz/tests/resources/mermaid/viz_shape_template.py:3: error: Module "ordeq_viz" has no attribute "pipeline_to_mermaid"  [attr-defined]
packages/ordeq-viz/tests/resources/mermaid/viz_shape_template.py:5: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/mermaid/viz_shape_template.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 2 errors in 1 file (checked 1 source file)

```