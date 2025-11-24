## Resource

```python
from example_project import nodes_with_inline_io
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes_with_inline_io))

```

## Output

```text
UnboundLocalError: cannot access local variable 'module_ref' where it is not associated with a value
  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_nodes_and_ios
    fqn = f"{module_ref}:<anonymous{idx}>"
             ^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest_json
    project_model = create_manifest(package)

  File "/packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py", line LINO, in <module>
    print(create_manifest_json(nodes_with_inline_io))
          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```