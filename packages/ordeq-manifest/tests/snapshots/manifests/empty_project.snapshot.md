## Resource

```python
import example_empty
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_empty))

```

## Output

```text
{
  "name": "example_empty",
  "nodes": {},
  "ios": {}
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/empty_project.py:1: error: Skipping analyzing "example_empty": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/empty_project.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```