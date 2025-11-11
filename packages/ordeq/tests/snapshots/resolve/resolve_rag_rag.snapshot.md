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
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(_resolve_runnables_to_nodes(*runnables)))

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
['example_rag_pipeline.rag.annotation:annotate_documents',
 'example_rag_pipeline.rag.evaluation:evaluate_answers',
 'example_rag_pipeline.rag.indexer:create_vector_index',
 'example_rag_pipeline.rag.policies:generate_questions',
 'example_rag_pipeline.rag.question_answering:question_answering',
 'example_rag_pipeline.rag.retrieval:filter_relevant',
 'example_rag_pipeline.rag.retrieval:retrieve']
{}
[('example_rag_pipeline.rag.annotation',
  'annotate_documents',
  Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)])),
 ('example_rag_pipeline.rag.evaluation',
  'evaluate_answers',
  Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID1), IO(idx=ID4)], outputs=[IO(idx=ID5)])),
 ('example_rag_pipeline.rag.indexer',
  'create_vector_index',
  Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID2), IO(idx=ID6)], outputs=[IO(idx=ID7)])),
 ('example_rag_pipeline.rag.policies',
  'generate_questions',
  Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID8)], outputs=[IO(idx=ID9)])),
 ('example_rag_pipeline.rag.question_answering',
  'question_answering',
  Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID9), IO(idx=ID10), IO(idx=ID4)], outputs=[IO(idx=ID1)])),
 ('example_rag_pipeline.rag.retrieval',
  'filter_relevant',
  Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID11), IO(idx=ID4)], outputs=[IO(idx=ID10)])),
 ('example_rag_pipeline.rag.retrieval',
  'retrieve',
  Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID7), IO(idx=ID9), IO(idx=ID6)], outputs=[IO(idx=ID11)]))]

```