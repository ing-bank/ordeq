## Resource

```python
from ordeq_manifest import create_manifest_json
from examples import empty

print(create_manifest_json(empty))

```

## Output

```text
{
  "name": "examples.empty",
  "nodes": {},
  "ios": {}
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/empty.py:2: error: Module "examples" has no attribute "empty"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```