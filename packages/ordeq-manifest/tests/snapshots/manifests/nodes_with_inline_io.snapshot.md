## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import nodes_with_inline_io

print(create_manifest_json(nodes_with_inline_io))

```

## Exception

```text
KeyError: Literal('Buenos dias')
  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_node
    inputs=[ios_to_id[i] for i in node.inputs],  # type: ignore[index,arg-type]
            ~~~~~~~~~^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_nodes_and_ios
    node.name: NodeModel.from_node(
               ~~~~~~~~~~~~~~~~~~~^
        str_to_fqn(node.name), node, ios_to_id
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest_json
    project_model = create_manifest(package)

  File "/packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py", line LINO, in <module>
    print(create_manifest_json(nodes_with_inline_io))
          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```