## Resource

```python
import tempfile
from pathlib import Path

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"

    viz(
        "example_rag_pipeline",
        fmt="mermaid",
        output=output_file,
        use_dataset_styles=True,
        legend=True,
        title="RAG Pipeline",
    )

    content = output_file.read_text()
    print(content)

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
		L00@{shape: rect, label: "IO"}
	end

	IO0 --> example_rag_pipeline.rag.annotation:annotate_documents
	IO1 --> example_rag_pipeline.rag.annotation:annotate_documents
	example_rag_pipeline.rag.annotation:annotate_documents --> IO2
	IO0 --> example_rag_pipeline.rag.evaluation:evaluate_answers
	IO3 --> example_rag_pipeline.rag.evaluation:evaluate_answers
	example_rag_pipeline.rag.evaluation:evaluate_answers --> IO4
	IO1 --> example_rag_pipeline.rag.indexer:create_vector_index
	IO5 --> example_rag_pipeline.rag.indexer:create_vector_index
	example_rag_pipeline.rag.indexer:create_vector_index --> IO6
	IO7 --> example_rag_pipeline.rag.policies:generate_questions
	example_rag_pipeline.rag.policies:generate_questions --> IO8
	IO8 --> example_rag_pipeline.rag.question_answering:question_answering
	IO9 --> example_rag_pipeline.rag.question_answering:question_answering
	IO3 --> example_rag_pipeline.rag.question_answering:question_answering
	example_rag_pipeline.rag.question_answering:question_answering --> IO0
	IO10 --> example_rag_pipeline.rag.retrieval:filter_relevant
	IO3 --> example_rag_pipeline.rag.retrieval:filter_relevant
	example_rag_pipeline.rag.retrieval:filter_relevant --> IO9
	IO6 --> example_rag_pipeline.rag.retrieval:retrieve
	IO8 --> example_rag_pipeline.rag.retrieval:retrieve
	IO5 --> example_rag_pipeline.rag.retrieval:retrieve
	example_rag_pipeline.rag.retrieval:retrieve --> IO10

	example_rag_pipeline.rag.annotation:annotate_documents@{shape: rounded, label: "annotate_documents"}
	example_rag_pipeline.rag.evaluation:evaluate_answers@{shape: rounded, label: "evaluate_answers"}
	example_rag_pipeline.rag.indexer:create_vector_index@{shape: rounded, label: "create_vector_index"}
	example_rag_pipeline.rag.policies:generate_questions@{shape: rounded, label: "generate_questions"}
	example_rag_pipeline.rag.question_answering:question_answering@{shape: rounded, label: "question_answering"}
	example_rag_pipeline.rag.retrieval:filter_relevant@{shape: rounded, label: "filter_relevant"}
	example_rag_pipeline.rag.retrieval:retrieve@{shape: rounded, label: "retrieve"}
	IO10@{shape: rect, label: "retrieved_pages"}
	IO0@{shape: rect, label: "llm_answers"}
	IO1@{shape: rect, label: "pdf_documents"}
	IO2@{shape: rect, label: "pdfs_documents_annotated"}
	IO3@{shape: rect, label: "llm_model"}
	IO4@{shape: rect, label: "metrics"}
	IO5@{shape: rect, label: "llm_vision_retrieval_model"}
	IO6@{shape: rect, label: "index"}
	IO7@{shape: rect, label: "policies"}
	IO8@{shape: rect, label: "questions"}
	IO9@{shape: rect, label: "relevant_pages"}

	class L0,example_rag_pipeline.rag.annotation:annotate_documents,example_rag_pipeline.rag.evaluation:evaluate_answers,example_rag_pipeline.rag.indexer:create_vector_index,example_rag_pipeline.rag.policies:generate_questions,example_rag_pipeline.rag.question_answering:question_answering,example_rag_pipeline.rag.retrieval:filter_relevant,example_rag_pipeline.rag.retrieval:retrieve node
	class L2 view
	class L00,IO10,IO0,IO1,IO2,IO3,IO4,IO5,IO6,IO7,IO8,IO9 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5


```