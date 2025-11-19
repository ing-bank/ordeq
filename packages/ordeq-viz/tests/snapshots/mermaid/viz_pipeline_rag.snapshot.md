## Resource

```python
from ordeq_viz import viz

diagram = viz(
    "example_rag_pipeline",
    fmt="mermaid",
    io_shape="cylinder",
    use_dataset_styles=True,
    legend=True,
    title="RAG Pipeline",
)
print(diagram)

```

## Output

```text
---
title: "RAG Pipeline"
---
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: cylinder, label: "IO"}
	end

	IO0 --> example_rag_pipeline.rag.indexer:create_vector_index
	IO1 --> example_rag_pipeline.rag.indexer:create_vector_index
	example_rag_pipeline.rag.indexer:create_vector_index --> IO2
	IO3 --> example_rag_pipeline.rag.policies:generate_questions
	example_rag_pipeline.rag.policies:generate_questions --> IO4
	IO2 --> example_rag_pipeline.rag.retrieval:retrieve
	IO4 --> example_rag_pipeline.rag.retrieval:retrieve
	IO1 --> example_rag_pipeline.rag.retrieval:retrieve
	example_rag_pipeline.rag.retrieval:retrieve --> IO5
	IO5 --> example_rag_pipeline.rag.retrieval:filter_relevant
	IO6 --> example_rag_pipeline.rag.retrieval:filter_relevant
	example_rag_pipeline.rag.retrieval:filter_relevant --> IO7
	IO4 --> example_rag_pipeline.rag.question_answering:question_answering
	IO7 --> example_rag_pipeline.rag.question_answering:question_answering
	IO6 --> example_rag_pipeline.rag.question_answering:question_answering
	example_rag_pipeline.rag.question_answering:question_answering --> IO8
	IO8 --> example_rag_pipeline.rag.evaluation:evaluate_answers
	IO6 --> example_rag_pipeline.rag.evaluation:evaluate_answers
	example_rag_pipeline.rag.evaluation:evaluate_answers --> IO9
	IO8 --> example_rag_pipeline.rag.annotation:annotate_documents
	IO0 --> example_rag_pipeline.rag.annotation:annotate_documents
	example_rag_pipeline.rag.annotation:annotate_documents --> IO10

	example_rag_pipeline.rag.indexer:create_vector_index@{shape: rounded, label: "create_vector_index"}
	example_rag_pipeline.rag.policies:generate_questions@{shape: rounded, label: "generate_questions"}
	example_rag_pipeline.rag.retrieval:retrieve@{shape: rounded, label: "retrieve"}
	example_rag_pipeline.rag.retrieval:filter_relevant@{shape: rounded, label: "filter_relevant"}
	IO5@{shape: cylinder, label: "retrieved_pages"}
	example_rag_pipeline.rag.question_answering:question_answering@{shape: rounded, label: "question_answering"}
	example_rag_pipeline.rag.evaluation:evaluate_answers@{shape: rounded, label: "evaluate_answers"}
	example_rag_pipeline.rag.annotation:annotate_documents@{shape: rounded, label: "annotate_documents"}
	IO0@{shape: cylinder, label: "pdf_documents"}
	IO1@{shape: cylinder, label: "llm_vision_retrieval_model"}
	IO10@{shape: cylinder, label: "pdfs_documents_annotated"}
	IO2@{shape: cylinder, label: "index"}
	IO3@{shape: cylinder, label: "policies"}
	IO4@{shape: cylinder, label: "questions"}
	IO6@{shape: cylinder, label: "llm_model"}
	IO7@{shape: cylinder, label: "relevant_pages"}
	IO8@{shape: cylinder, label: "llm_answers"}
	IO9@{shape: cylinder, label: "metrics"}

	class L0,example_rag_pipeline.rag.indexer:create_vector_index,example_rag_pipeline.rag.policies:generate_questions,example_rag_pipeline.rag.retrieval:retrieve,example_rag_pipeline.rag.retrieval:filter_relevant,example_rag_pipeline.rag.question_answering:question_answering,example_rag_pipeline.rag.evaluation:evaluate_answers,example_rag_pipeline.rag.annotation:annotate_documents node
	class L00,IO5,IO0,IO1,IO10,IO2,IO3,IO4,IO6,IO7,IO8,IO9 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```