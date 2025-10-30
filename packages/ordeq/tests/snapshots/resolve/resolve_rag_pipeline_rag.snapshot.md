## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("examples.rag_pipeline"),
    importlib.import_module("examples.rag_pipeline.rag"),
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
['examples.rag_pipeline', 'examples.rag_pipeline.catalog', 'examples.rag_pipeline.rag', 'examples.rag_pipeline.rag.annotation', 'examples.rag_pipeline.rag.evaluation', 'examples.rag_pipeline.rag.indexer', 'examples.rag_pipeline.rag.policies', 'examples.rag_pipeline.rag.question_answering', 'examples.rag_pipeline.rag.retrieval']
['examples.rag_pipeline.rag.annotation:annotate_documents', 'examples.rag_pipeline.rag.evaluation:evaluate_answers', 'examples.rag_pipeline.rag.indexer:create_vector_index', 'examples.rag_pipeline.rag.policies:generate_questions', 'examples.rag_pipeline.rag.question_answering:question_answering', 'examples.rag_pipeline.rag.retrieval:filter_relevant', 'examples.rag_pipeline.rag.retrieval:retrieve']
{('examples.rag_pipeline.catalog', 'index'): IO(idx=ID1), ('examples.rag_pipeline.catalog', 'llm_answers'): IO(idx=ID2), ('examples.rag_pipeline.catalog', 'llm_model'): IO(idx=ID3), ('examples.rag_pipeline.catalog', 'llm_vision_retrieval_model'): IO(idx=ID4), ('examples.rag_pipeline.catalog', 'metrics'): IO(idx=ID5), ('examples.rag_pipeline.catalog', 'pdf_documents'): IO(idx=ID6), ('examples.rag_pipeline.catalog', 'pdfs_documents_annotated'): IO(idx=ID7), ('examples.rag_pipeline.catalog', 'policies'): IO(idx=ID8), ('examples.rag_pipeline.catalog', 'questions'): IO(idx=ID9), ('examples.rag_pipeline.catalog', 'relevant_pages'): IO(idx=ID10), ('examples.rag_pipeline.catalog', 'retrieved_pages'): IO(idx=ID11)}
['examples.rag_pipeline.rag.annotation:annotate_documents', 'examples.rag_pipeline.rag.evaluation:evaluate_answers', 'examples.rag_pipeline.rag.indexer:create_vector_index', 'examples.rag_pipeline.rag.policies:generate_questions', 'examples.rag_pipeline.rag.question_answering:question_answering', 'examples.rag_pipeline.rag.retrieval:filter_relevant', 'examples.rag_pipeline.rag.retrieval:retrieve']

```