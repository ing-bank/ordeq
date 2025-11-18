## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_rag_pipeline.rag")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_rag_pipeline.rag',
 'example_rag_pipeline.rag.annotation',
 'example_rag_pipeline.rag.evaluation',
 'example_rag_pipeline.rag.indexer',
 'example_rag_pipeline.rag.policies',
 'example_rag_pipeline.rag.question_answering',
 'example_rag_pipeline.rag.retrieval']
[('example_rag_pipeline.rag.annotation',
  'annotate_documents',
  Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)])),
 ('example_rag_pipeline.rag.evaluation',
  'evaluate_answers',
  Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)])),
 ('example_rag_pipeline.rag.indexer',
  'create_vector_index',
  Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)])),
 ('example_rag_pipeline.rag.policies',
  'generate_questions',
  Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)])),
 ('example_rag_pipeline.rag.question_answering',
  'question_answering',
  Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)])),
 ('example_rag_pipeline.rag.retrieval',
  'retrieve',
  Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])),
 ('example_rag_pipeline.rag.retrieval',
  'filter_relevant',
  Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]))]
{}
[('example_rag_pipeline.rag.annotation',
  'annotate_documents',
  Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)])),
 ('example_rag_pipeline.rag.evaluation',
  'evaluate_answers',
  Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)])),
 ('example_rag_pipeline.rag.indexer',
  'create_vector_index',
  Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)])),
 ('example_rag_pipeline.rag.policies',
  'generate_questions',
  Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)])),
 ('example_rag_pipeline.rag.question_answering',
  'question_answering',
  Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)])),
 ('example_rag_pipeline.rag.retrieval',
  'retrieve',
  Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])),
 ('example_rag_pipeline.rag.retrieval',
  'filter_relevant',
  Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]))]

```