## Resource

```python
from ordeq_manifest import create_manifest_json
from project import misc

print(create_manifest_json(misc))

```

## Output

```text
{
  "name": "project.misc",
  "nodes": {},
  "ios": {}
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/misc.py:2: error: Module "project" has no attribute "misc"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```