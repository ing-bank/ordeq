## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NamedNodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
print(named_node_io_graph)

named_node_graph = NamedNodeGraph.from_graph(named_node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)

```

## Output

```text
NamedNodeIOGraph:
io-0 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
io-0 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-1 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
io-1 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-3 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-3 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-3 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
io-5 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-5 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-7 --> Node:example_rag_pipeline.rag.policies:generate_questions
io-8 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-8 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-9 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-10 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
io-6 --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.annotation:annotate_documents --> io-2
Node:example_rag_pipeline.rag.evaluation:evaluate_answers --> io-4
Node:example_rag_pipeline.rag.indexer:create_vector_index --> io-6
Node:example_rag_pipeline.rag.policies:generate_questions --> io-8
Node:example_rag_pipeline.rag.question_answering:question_answering --> io-0
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> io-9
Node:example_rag_pipeline.rag.retrieval:retrieve --> io-10
NamedNodeGraph:
Node:example_rag_pipeline.rag.indexer:create_vector_index --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.annotation:annotate_documents
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.retrieval:retrieve --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
Topological ordering:
(Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]),
 Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID3), IO(idx=ID4)], outputs=[IO(idx=ID5)]),
 Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID5), IO(idx=ID2), IO(idx=ID4)], outputs=[IO(idx=ID6)]),
 Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID8)]),
 Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID2), IO(idx=ID8), IO(idx=ID7)], outputs=[IO(idx=ID9)]),
 Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID9), IO(idx=ID7)], outputs=[IO(idx=ID10)]),
 Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID9), IO(idx=ID3)], outputs=[IO(idx=ID11)]))

```