## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import nodes_with_inline_io

print(create_manifest_json(nodes_with_inline_io))

```

## Exception

```text
KeyError: Literal('Buenos dias')
```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```