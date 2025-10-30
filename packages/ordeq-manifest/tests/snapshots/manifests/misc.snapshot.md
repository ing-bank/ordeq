## Resource

```python
from example_project import misc
from ordeq_manifest import create_manifest_json

print(create_manifest_json(misc))

```

## Output

```text
{
  "name": "example_project.misc",
  "nodes": {},
  "ios": {}
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/misc.py:1: error: Skipping analyzing "example_project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/misc.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```