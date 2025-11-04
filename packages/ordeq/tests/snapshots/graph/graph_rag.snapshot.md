## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
base_graph = NodeIOGraph.from_nodes(nodes)
print(base_graph)
node_graph = NodeGraph.from_graph(base_graph)
pprint(node_graph.topological_ordering)

```

## Output

```text
Node:example_rag_pipeline.rag.annotation:annotate_documents --> io-1
Node:example_rag_pipeline.rag.evaluation:evaluate_answers --> io-2
Node:example_rag_pipeline.rag.indexer:create_vector_index --> io-3
io-3 --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.policies:generate_questions --> io-4
io-4 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-4 --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.question_answering:question_answering --> io-5
io-5 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
io-5 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> io-6
io-6 --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.retrieval:retrieve --> io-7
io-7 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
(Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]),
 Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID3), IO(idx=ID4)], outputs=[IO(idx=ID5)]),
 Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID5), IO(idx=ID2), IO(idx=ID4)], outputs=[IO(idx=ID6)]),
 Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID8)]),
 Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID2), IO(idx=ID8), IO(idx=ID7)], outputs=[IO(idx=ID9)]),
 Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID9), IO(idx=ID7)], outputs=[IO(idx=ID10)]),
 Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID9), IO(idx=ID3)], outputs=[IO(idx=ID11)]))

```