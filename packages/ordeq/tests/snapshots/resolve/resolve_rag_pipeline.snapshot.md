## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("rag_pipeline"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(list(sorted(node.name for node in nodes)))
oprint(dict(sorted(ios.items())))

print(list(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables))))

```

## Exception

```text
NameError: name 'oprint' is not defined
  File "/packages/ordeq/tests/resources/resolve/resolve_rag_pipeline.py", line 17, in <module>
    oprint(dict(sorted(ios.items())))
    ^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
['rag_pipeline', 'rag_pipeline.catalog', 'rag_pipeline.rag', 'rag_pipeline.rag.annotation', 'rag_pipeline.rag.evaluation', 'rag_pipeline.rag.indexer', 'rag_pipeline.rag.policies', 'rag_pipeline.rag.question_answering', 'rag_pipeline.rag.retrieval']
['rag_pipeline.rag.annotation:annotate_documents', 'rag_pipeline.rag.evaluation:evaluate_answers', 'rag_pipeline.rag.indexer:create_vector_index', 'rag_pipeline.rag.policies:generate_questions', 'rag_pipeline.rag.question_answering:question_answering', 'rag_pipeline.rag.retrieval:filter_relevant', 'rag_pipeline.rag.retrieval:retrieve']

```

## Typing

```text
packages/ordeq/tests/resources/resolve/resolve_rag_pipeline.py:17: error: Name "oprint" is not defined  [name-defined]
Found 1 error in 1 file (checked 1 source file)

```