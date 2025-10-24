## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("rag_pipeline.rag.annotation"),
    importlib.import_module("rag_pipeline.rag.evaluation"),
    importlib.import_module("rag_pipeline.rag.indexer"),
    importlib.import_module("rag_pipeline.rag.policies"),
    importlib.import_module("rag_pipeline.rag.question_answering"),
    importlib.import_module("rag_pipeline.rag.retrieval"),
    importlib.import_module("rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(list(sorted(node.name for node in nodes)))
print(list(ios.keys()))

print(list(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables))))

```

## Output

```text
['rag_pipeline.rag.annotation', 'rag_pipeline.rag.evaluation', 'rag_pipeline.rag.indexer', 'rag_pipeline.rag.policies', 'rag_pipeline.rag.question_answering', 'rag_pipeline.rag.retrieval', 'rag_pipeline.catalog']
['rag_pipeline.rag.annotation:annotate_documents', 'rag_pipeline.rag.evaluation:evaluate_answers', 'rag_pipeline.rag.indexer:create_vector_index', 'rag_pipeline.rag.policies:generate_questions', 'rag_pipeline.rag.question_answering:question_answering', 'rag_pipeline.rag.retrieval:filter_relevant', 'rag_pipeline.rag.retrieval:retrieve']
[('rag_pipeline.catalog', 'policies'), ('rag_pipeline.catalog', 'llm_model'), ('rag_pipeline.catalog', 'llm_vision_retrieval_model'), ('rag_pipeline.catalog', 'pdf_documents'), ('rag_pipeline.catalog', 'retrieved_pages'), ('rag_pipeline.catalog', 'relevant_pages'), ('rag_pipeline.catalog', 'index'), ('rag_pipeline.catalog', 'questions'), ('rag_pipeline.catalog', 'metrics'), ('rag_pipeline.catalog', 'pdfs_documents_annotated'), ('rag_pipeline.catalog', 'llm_answers')]
['rag_pipeline.rag.annotation:annotate_documents', 'rag_pipeline.rag.evaluation:evaluate_answers', 'rag_pipeline.rag.indexer:create_vector_index', 'rag_pipeline.rag.policies:generate_questions', 'rag_pipeline.rag.question_answering:question_answering', 'rag_pipeline.rag.retrieval:filter_relevant', 'rag_pipeline.rag.retrieval:retrieve']

```