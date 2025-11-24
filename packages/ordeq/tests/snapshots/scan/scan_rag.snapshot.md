## Resource

```python
from pprint import pprint

import example_rag_pipeline
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_rag_pipeline)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[Node(module=example_rag_pipeline.rag.annotation, name=annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)]),
 Node(module=example_rag_pipeline.rag.evaluation, name=evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)]),
 Node(module=example_rag_pipeline.rag.indexer, name=create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)]),
 Node(module=example_rag_pipeline.rag.policies, name=generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)]),
 Node(module=example_rag_pipeline.rag.question_answering, name=question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)]),
 Node(module=example_rag_pipeline.rag.retrieval, name=filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]),
 Node(module=example_rag_pipeline.rag.retrieval, name=retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])]
IOs:
[[FQN(module='example_rag_pipeline.catalog', name='policies')],
 [FQN(module='example_rag_pipeline.catalog', name='llm_model')],
 [FQN(module='example_rag_pipeline.catalog', name='llm_vision_retrieval_model')],
 [FQN(module='example_rag_pipeline.catalog', name='pdf_documents')],
 [FQN(module='example_rag_pipeline.catalog', name='retrieved_pages')],
 [FQN(module='example_rag_pipeline.catalog', name='relevant_pages')],
 [FQN(module='example_rag_pipeline.catalog', name='index')],
 [FQN(module='example_rag_pipeline.catalog', name='questions')],
 [FQN(module='example_rag_pipeline.catalog', name='metrics')],
 [FQN(module='example_rag_pipeline.catalog', name='pdfs_documents_annotated')],
 [FQN(module='example_rag_pipeline.catalog', name='llm_answers')]]

```