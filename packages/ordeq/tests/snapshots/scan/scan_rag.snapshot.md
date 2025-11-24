## Resource

```python
from pprint import pprint

import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_rag_pipeline))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='example_rag_pipeline.rag.annotation', name='annotate_documents'),
  Node(module=example_rag_pipeline.rag.annotation, name=annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)])),
 (FQN(module='example_rag_pipeline.rag.evaluation', name='evaluate_answers'),
  Node(module=example_rag_pipeline.rag.evaluation, name=evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)])),
 (FQN(module='example_rag_pipeline.rag.indexer', name='create_vector_index'),
  Node(module=example_rag_pipeline.rag.indexer, name=create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)])),
 (FQN(module='example_rag_pipeline.rag.policies', name='generate_questions'),
  Node(module=example_rag_pipeline.rag.policies, name=generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)])),
 (FQN(module='example_rag_pipeline.rag.question_answering', name='question_answering'),
  Node(module=example_rag_pipeline.rag.question_answering, name=question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='retrieve'),
  Node(module=example_rag_pipeline.rag.retrieval, name=retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='filter_relevant'),
  Node(module=example_rag_pipeline.rag.retrieval, name=filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]))]
IOs:
[(FQN(module='example_rag_pipeline.catalog', name='policies'),
  IO(id=ID8)),
 (FQN(module='example_rag_pipeline.catalog', name='llm_model'),
  IO(id=ID4)),
 (FQN(module='example_rag_pipeline.catalog', name='llm_vision_retrieval_model'),
  IO(id=ID6)),
 (FQN(module='example_rag_pipeline.catalog', name='pdf_documents'),
  IO(id=ID2)),
 (FQN(module='example_rag_pipeline.catalog', name='retrieved_pages'),
  IO(id=ID11)),
 (FQN(module='example_rag_pipeline.catalog', name='relevant_pages'),
  IO(id=ID10)),
 (FQN(module='example_rag_pipeline.catalog', name='index'),
  IO(id=ID7)),
 (FQN(module='example_rag_pipeline.catalog', name='questions'),
  IO(id=ID9)),
 (FQN(module='example_rag_pipeline.catalog', name='metrics'),
  IO(id=ID5)),
 (FQN(module='example_rag_pipeline.catalog', name='pdfs_documents_annotated'),
  IO(id=ID3)),
 (FQN(module='example_rag_pipeline.catalog', name='llm_answers'),
  IO(id=ID1))]

```