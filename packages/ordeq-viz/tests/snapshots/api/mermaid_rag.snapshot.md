## Resource

```python
import tempfile
from pathlib import Path

import rag_pipeline  # ty: ignore[unresolved-import]  # noqa: F401,RUF100
from ordeq_viz import viz


with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"

    viz(
        "rag_pipeline",
        fmt="mermaid",
        output=output_file,
        io_shape_template="({value})",
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
		subgraph Objects
			L0(["Node"]):::node
			L1(IO):::io
		end
		subgraph IO Types
			L00(FaissIndex):::io0
			L01(IO):::io1
			L02(PandasExcel):::io2
			L03(Pickle):::io3
			L04(PymupdfFile):::io4
			L05(SentenceTransformer):::io5
		end
	end

	IO0 --> rag_pipeline.rag.policies:generate_questions
	rag_pipeline.rag.policies:generate_questions --> IO1
	IO2 --> rag_pipeline.rag.indexer:create_vector_index
	IO3 --> rag_pipeline.rag.indexer:create_vector_index
	rag_pipeline.rag.indexer:create_vector_index --> IO4
	IO4 --> rag_pipeline.rag.retrieval:retrieve
	IO1 --> rag_pipeline.rag.retrieval:retrieve
	IO3 --> rag_pipeline.rag.retrieval:retrieve
	rag_pipeline.rag.retrieval:retrieve --> IO5
	IO5 --> rag_pipeline.rag.retrieval:filter_relevant
	IO6 --> rag_pipeline.rag.retrieval:filter_relevant
	rag_pipeline.rag.retrieval:filter_relevant --> IO7
	IO1 --> rag_pipeline.rag.question_answering:question_answering
	IO7 --> rag_pipeline.rag.question_answering:question_answering
	IO6 --> rag_pipeline.rag.question_answering:question_answering
	rag_pipeline.rag.question_answering:question_answering --> IO8
	IO8 --> rag_pipeline.rag.evaluation:evaluate_answers
	IO6 --> rag_pipeline.rag.evaluation:evaluate_answers
	rag_pipeline.rag.evaluation:evaluate_answers --> IO9
	IO8 --> rag_pipeline.rag.annotation:annotate_documents
	IO2 --> rag_pipeline.rag.annotation:annotate_documents
	rag_pipeline.rag.annotation:annotate_documents --> IO10

	subgraph pipeline["Pipeline"]
		direction TB
		rag_pipeline.rag.policies:generate_questions(["generate_questions"]):::node
		rag_pipeline.rag.indexer:create_vector_index(["create_vector_index"]):::node
		rag_pipeline.rag.retrieval:retrieve(["retrieve"]):::node
		rag_pipeline.rag.retrieval:filter_relevant(["filter_relevant"]):::node
		rag_pipeline.rag.question_answering:question_answering(["question_answering"]):::node
		rag_pipeline.rag.evaluation:evaluate_answers(["evaluate_answers"]):::node
		rag_pipeline.rag.annotation:annotate_documents(["annotate_documents"]):::node
		IO0(policies):::io2
		IO1(questions):::io1
		IO2(pdf_documents):::io4
		IO3(llm_vision_retrieval_model):::io5
		IO4(index):::io0
		IO5(retrieved_pages):::io1
		IO6(llm_model):::io5
		IO7(relevant_pages):::io1
		IO8(llm_answers):::io1
		IO9(metrics):::io3
		IO10(pdfs_documents_annotated):::io4
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f


```

## Typing

```text
packages/ordeq-viz/tests/resources/api/mermaid_rag.py:4: error: Skipping analyzing "rag_pipeline": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_rag.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```