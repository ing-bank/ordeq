## Resource

```python
from ordeq_manifest import create_manifest_json
import examples.project

print(create_manifest_json(examples.project))

```

## Exception

```text
KeyError: Literal('Buenos dias')
  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line 47, in from_node
    inputs=[ios_to_id[i] for i in node.inputs],  # type: ignore[index,arg-type]
            ~~~~~~~~~^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line 88, in from_nodes_and_ios
    f"nodes.{node.name}": NodeModel.from_node(
                          ~~~~~~~~~~~~~~~~~~~^
        ("nodes", node.name), node, ios_to_id
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line 65, in create_manifest
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line 45, in create_manifest_json
    project_model = create_manifest(package)

  File "/packages/ordeq-manifest/tests/resources/manifests/project.py", line 4, in <module>
    print(create_manifest_json(examples.project))
          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/project.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/project.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```