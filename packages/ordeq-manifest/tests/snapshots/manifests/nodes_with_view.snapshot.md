## Resource

```python
from example_project import nodes_with_view
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes_with_view))

```

## Exception

```text
AttributeError: 'View' object has no attribute 'references'
  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_io
    references=list(io.references.keys()),
                    ^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_nodes_and_ios
    model = IOModel.from_io(((mod, f"<anonymous{idx}>"), obj))  # type: ignore[arg-type]

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest_json
    project_model = create_manifest(package)

  File "/packages/ordeq-manifest/tests/resources/manifests/nodes_with_view.py", line LINO, in <module>
    print(create_manifest_json(nodes_with_view))
          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```