## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_rag_pipeline.rag.annotation"),
    importlib.import_module("example_rag_pipeline.rag.evaluation"),
    importlib.import_module("example_rag_pipeline.rag.indexer"),
    importlib.import_module("example_rag_pipeline.rag.policies"),
    importlib.import_module("example_rag_pipeline.rag.question_answering"),
    importlib.import_module("example_rag_pipeline.rag.retrieval"),
    importlib.import_module("example_rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(list(ios.keys()))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_rag_pipeline.rag.annotation', 'example_rag_pipeline.rag.evaluation', 'example_rag_pipeline.rag.indexer', 'example_rag_pipeline.rag.policies', 'example_rag_pipeline.rag.question_answering', 'example_rag_pipeline.rag.retrieval', 'example_rag_pipeline.catalog']
['example_rag_pipeline.rag.annotation:annotate_documents', 'example_rag_pipeline.rag.evaluation:evaluate_answers', 'example_rag_pipeline.rag.indexer:create_vector_index', 'example_rag_pipeline.rag.policies:generate_questions', 'example_rag_pipeline.rag.question_answering:question_answering', 'example_rag_pipeline.rag.retrieval:filter_relevant', 'example_rag_pipeline.rag.retrieval:retrieve']
[('example_rag_pipeline.catalog', 'policies'), ('example_rag_pipeline.catalog', 'llm_model'), ('example_rag_pipeline.catalog', 'llm_vision_retrieval_model'), ('example_rag_pipeline.catalog', 'pdf_documents'), ('example_rag_pipeline.catalog', 'retrieved_pages'), ('example_rag_pipeline.catalog', 'relevant_pages'), ('example_rag_pipeline.catalog', 'index'), ('example_rag_pipeline.catalog', 'questions'), ('example_rag_pipeline.catalog', 'metrics'), ('example_rag_pipeline.catalog', 'pdfs_documents_annotated'), ('example_rag_pipeline.catalog', 'llm_answers')]
['example_rag_pipeline.rag.annotation:annotate_documents', 'example_rag_pipeline.rag.evaluation:evaluate_answers', 'example_rag_pipeline.rag.indexer:create_vector_index', 'example_rag_pipeline.rag.policies:generate_questions', 'example_rag_pipeline.rag.question_answering:question_answering', 'example_rag_pipeline.rag.retrieval:filter_relevant', 'example_rag_pipeline.rag.retrieval:retrieve']

```