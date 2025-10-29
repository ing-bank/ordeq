## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("rag_pipeline.rag.annotation"),
    importlib.import_module("rag_pipeline.rag.evaluation"),
    importlib.import_module("rag_pipeline.rag.indexer"),
    importlib.import_module("rag_pipeline.rag.policies"),
    importlib.import_module("rag_pipeline.rag.question_answering"),
    importlib.import_module("rag_pipeline.rag.retrieval"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['rag_pipeline.rag.annotation', 'rag_pipeline.rag.evaluation', 'rag_pipeline.rag.indexer', 'rag_pipeline.rag.policies', 'rag_pipeline.rag.question_answering', 'rag_pipeline.rag.retrieval']
['rag_pipeline.rag.annotation:annotate_documents', 'rag_pipeline.rag.evaluation:evaluate_answers', 'rag_pipeline.rag.indexer:create_vector_index', 'rag_pipeline.rag.policies:generate_questions', 'rag_pipeline.rag.question_answering:question_answering', 'rag_pipeline.rag.retrieval:filter_relevant', 'rag_pipeline.rag.retrieval:retrieve']
{}
['rag_pipeline.rag.annotation:annotate_documents', 'rag_pipeline.rag.evaluation:evaluate_answers', 'rag_pipeline.rag.indexer:create_vector_index', 'rag_pipeline.rag.policies:generate_questions', 'rag_pipeline.rag.question_answering:question_answering', 'rag_pipeline.rag.retrieval:filter_relevant', 'rag_pipeline.rag.retrieval:retrieve']

```