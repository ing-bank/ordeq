## Resource

```python
from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("rag_pipeline.rag"),
    importlib.import_module("rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(dict(sorted(nodes.items())))
print(dict(sorted(ios.items())))

print(dict(sorted(_resolve_runnables_to_nodes(*runnables).items())))

```

## Output

```text
['rag_pipeline.rag', 'rag_pipeline.rag.annotation', 'rag_pipeline.rag.evaluation', 'rag_pipeline.rag.indexer', 'rag_pipeline.rag.policies', 'rag_pipeline.rag.question_answering', 'rag_pipeline.rag.retrieval', 'rag_pipeline.catalog']
{('rag_pipeline.rag.annotation', 'annotate_documents'): Node(name=rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)]), ('rag_pipeline.rag.evaluation', 'evaluate_answers'): Node(name=rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID1), IO(idx=ID4)], outputs=[IO(idx=ID5)]), ('rag_pipeline.rag.indexer', 'create_vector_index'): Node(name=rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID2), IO(idx=ID6)], outputs=[IO(idx=ID7)]), ('rag_pipeline.rag.policies', 'generate_questions'): Node(name=rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID8)], outputs=[IO(idx=ID9)]), ('rag_pipeline.rag.question_answering', 'question_answering'): Node(name=rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID9), IO(idx=ID10), IO(idx=ID4)], outputs=[IO(idx=ID1)]), ('rag_pipeline.rag.retrieval', 'filter_relevant'): Node(name=rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID11), IO(idx=ID4)], outputs=[IO(idx=ID10)]), ('rag_pipeline.rag.retrieval', 'retrieve'): Node(name=rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID7), IO(idx=ID9), IO(idx=ID6)], outputs=[IO(idx=ID11)])}
{('rag_pipeline.catalog', 'index'): IO(idx=ID7), ('rag_pipeline.catalog', 'llm_answers'): IO(idx=ID1), ('rag_pipeline.catalog', 'llm_model'): IO(idx=ID4), ('rag_pipeline.catalog', 'llm_vision_retrieval_model'): IO(idx=ID6), ('rag_pipeline.catalog', 'metrics'): IO(idx=ID5), ('rag_pipeline.catalog', 'pdf_documents'): IO(idx=ID2), ('rag_pipeline.catalog', 'pdfs_documents_annotated'): IO(idx=ID3), ('rag_pipeline.catalog', 'policies'): IO(idx=ID8), ('rag_pipeline.catalog', 'questions'): IO(idx=ID9), ('rag_pipeline.catalog', 'relevant_pages'): IO(idx=ID10), ('rag_pipeline.catalog', 'retrieved_pages'): IO(idx=ID11)}
{('rag_pipeline.rag.annotation', 'annotate_documents'): Node(name=rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)]), ('rag_pipeline.rag.evaluation', 'evaluate_answers'): Node(name=rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID1), IO(idx=ID4)], outputs=[IO(idx=ID5)]), ('rag_pipeline.rag.indexer', 'create_vector_index'): Node(name=rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID2), IO(idx=ID6)], outputs=[IO(idx=ID7)]), ('rag_pipeline.rag.policies', 'generate_questions'): Node(name=rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID8)], outputs=[IO(idx=ID9)]), ('rag_pipeline.rag.question_answering', 'question_answering'): Node(name=rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID9), IO(idx=ID10), IO(idx=ID4)], outputs=[IO(idx=ID1)]), ('rag_pipeline.rag.retrieval', 'filter_relevant'): Node(name=rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID11), IO(idx=ID4)], outputs=[IO(idx=ID10)]), ('rag_pipeline.rag.retrieval', 'retrieve'): Node(name=rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID7), IO(idx=ID9), IO(idx=ID6)], outputs=[IO(idx=ID11)])}

```