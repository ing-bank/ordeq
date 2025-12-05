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
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: cylinder, label: "IO"}
	end

	example_rag_pipeline.catalog:policies --> example_rag_pipeline.rag.policies:generate_questions
	example_rag_pipeline.rag.policies:generate_questions --> example_rag_pipeline.catalog:questions
	example_rag_pipeline.catalog:pdf_documents --> example_rag_pipeline.rag.indexer:create_vector_index
	example_rag_pipeline.catalog:llm_vision_retrieval_model --> example_rag_pipeline.rag.indexer:create_vector_index
	example_rag_pipeline.rag.indexer:create_vector_index --> example_rag_pipeline.catalog:index
	example_rag_pipeline.catalog:index --> example_rag_pipeline.rag.retrieval:retrieve
	example_rag_pipeline.catalog:questions --> example_rag_pipeline.rag.retrieval:retrieve
	example_rag_pipeline.catalog:llm_vision_retrieval_model --> example_rag_pipeline.rag.retrieval:retrieve
	example_rag_pipeline.rag.retrieval:retrieve --> example_rag_pipeline.catalog:retrieved_pages
	example_rag_pipeline.catalog:retrieved_pages --> example_rag_pipeline.rag.retrieval:filter_relevant
	example_rag_pipeline.catalog:llm_model --> example_rag_pipeline.rag.retrieval:filter_relevant
	example_rag_pipeline.rag.retrieval:filter_relevant --> example_rag_pipeline.catalog:relevant_pages
	example_rag_pipeline.catalog:questions --> example_rag_pipeline.rag.question_answering:question_answering
	example_rag_pipeline.catalog:relevant_pages --> example_rag_pipeline.rag.question_answering:question_answering
	example_rag_pipeline.catalog:llm_model --> example_rag_pipeline.rag.question_answering:question_answering
	example_rag_pipeline.rag.question_answering:question_answering --> example_rag_pipeline.catalog:llm_answers
	example_rag_pipeline.catalog:llm_answers --> example_rag_pipeline.rag.evaluation:evaluate_answers
	example_rag_pipeline.catalog:llm_model --> example_rag_pipeline.rag.evaluation:evaluate_answers
	example_rag_pipeline.rag.evaluation:evaluate_answers --> example_rag_pipeline.catalog:metrics
	example_rag_pipeline.catalog:llm_answers --> example_rag_pipeline.rag.annotation:annotate_documents
	example_rag_pipeline.catalog:pdf_documents --> example_rag_pipeline.rag.annotation:annotate_documents
	example_rag_pipeline.rag.annotation:annotate_documents --> example_rag_pipeline.catalog:pdfs_documents_annotated

	example_rag_pipeline.rag.policies:generate_questions@{shape: rounded, label: "generate_questions"}
	example_rag_pipeline.rag.indexer:create_vector_index@{shape: rounded, label: "create_vector_index"}
	example_rag_pipeline.rag.retrieval:retrieve@{shape: rounded, label: "retrieve"}
	example_rag_pipeline.rag.retrieval:filter_relevant@{shape: rounded, label: "filter_relevant"}
	example_rag_pipeline.catalog:retrieved_pages@{shape: cylinder, label: "retrieved_pages"}
	example_rag_pipeline.rag.question_answering:question_answering@{shape: rounded, label: "question_answering"}
	example_rag_pipeline.rag.evaluation:evaluate_answers@{shape: rounded, label: "evaluate_answers"}
	example_rag_pipeline.rag.annotation:annotate_documents@{shape: rounded, label: "annotate_documents"}
	example_rag_pipeline.catalog:index@{shape: cylinder, label: "index"}
	example_rag_pipeline.catalog:llm_answers@{shape: cylinder, label: "llm_answers"}
	example_rag_pipeline.catalog:llm_model@{shape: cylinder, label: "llm_model"}
	example_rag_pipeline.catalog:llm_vision_retrieval_model@{shape: cylinder, label: "llm_vision_retrieval_model"}
	example_rag_pipeline.catalog:metrics@{shape: cylinder, label: "metrics"}
	example_rag_pipeline.catalog:pdf_documents@{shape: cylinder, label: "pdf_documents"}
	example_rag_pipeline.catalog:pdfs_documents_annotated@{shape: cylinder, label: "pdfs_documents_annotated"}
	example_rag_pipeline.catalog:policies@{shape: cylinder, label: "policies"}
	example_rag_pipeline.catalog:questions@{shape: cylinder, label: "questions"}
	example_rag_pipeline.catalog:relevant_pages@{shape: cylinder, label: "relevant_pages"}

	class node_type,example_rag_pipeline.rag.policies:generate_questions,example_rag_pipeline.rag.indexer:create_vector_index,example_rag_pipeline.rag.retrieval:retrieve,example_rag_pipeline.rag.retrieval:filter_relevant,example_rag_pipeline.rag.question_answering:question_answering,example_rag_pipeline.rag.evaluation:evaluate_answers,example_rag_pipeline.rag.annotation:annotate_documents node
	class io_type_0,example_rag_pipeline.catalog:retrieved_pages,example_rag_pipeline.catalog:index,example_rag_pipeline.catalog:llm_answers,example_rag_pipeline.catalog:llm_model,example_rag_pipeline.catalog:llm_vision_retrieval_model,example_rag_pipeline.catalog:metrics,example_rag_pipeline.catalog:pdf_documents,example_rag_pipeline.catalog:pdfs_documents_annotated,example_rag_pipeline.catalog:policies,example_rag_pipeline.catalog:questions,example_rag_pipeline.catalog:relevant_pages io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```