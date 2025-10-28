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
		subgraph objects["Objects"]
			L0(["Node"]):::node
			L1(IO):::io
		end
		subgraph io_types["IO Types"]
			ordeq._io:IO(IO):::io0
			ordeq_faiss.index:FaissIndex(FaissIndex):::io1
			ordeq_files.pickle:Pickle(Pickle):::io2
			ordeq_pandas.excel:PandasExcel(PandasExcel):::io3
			ordeq_pymupdf.pdf_file:PymupdfFile(PymupdfFile):::io4
			ordeq_sentence_transformers.sentence_transformer:SentenceTransformer(SentenceTransformer):::io5
		end
	end

	rag_pipeline.catalog:llm_answers --> rag_pipeline.rag.annotation:annotate_documents
	rag_pipeline.catalog:pdf_documents --> rag_pipeline.rag.annotation:annotate_documents
	rag_pipeline.rag.annotation:annotate_documents --> rag_pipeline.catalog:pdfs_documents_annotated
	rag_pipeline.catalog:llm_answers --> rag_pipeline.rag.evaluation:evaluate_answers
	rag_pipeline.catalog:llm_model --> rag_pipeline.rag.evaluation:evaluate_answers
	rag_pipeline.rag.evaluation:evaluate_answers --> rag_pipeline.catalog:metrics
	rag_pipeline.catalog:pdf_documents --> rag_pipeline.rag.indexer:create_vector_index
	rag_pipeline.catalog:llm_vision_retrieval_model --> rag_pipeline.rag.indexer:create_vector_index
	rag_pipeline.rag.indexer:create_vector_index --> rag_pipeline.catalog:index
	rag_pipeline.catalog:policies --> rag_pipeline.rag.policies:generate_questions
	rag_pipeline.rag.policies:generate_questions --> rag_pipeline.catalog:questions
	rag_pipeline.catalog:questions --> rag_pipeline.rag.question_answering:question_answering
	rag_pipeline.catalog:relevant_pages --> rag_pipeline.rag.question_answering:question_answering
	rag_pipeline.catalog:llm_model --> rag_pipeline.rag.question_answering:question_answering
	rag_pipeline.rag.question_answering:question_answering --> rag_pipeline.catalog:llm_answers
	rag_pipeline.catalog:retrieved_pages --> rag_pipeline.rag.retrieval:filter_relevant
	rag_pipeline.catalog:llm_model --> rag_pipeline.rag.retrieval:filter_relevant
	rag_pipeline.rag.retrieval:filter_relevant --> rag_pipeline.catalog:relevant_pages
	rag_pipeline.catalog:index --> rag_pipeline.rag.retrieval:retrieve
	rag_pipeline.catalog:questions --> rag_pipeline.rag.retrieval:retrieve
	rag_pipeline.catalog:llm_vision_retrieval_model --> rag_pipeline.rag.retrieval:retrieve
	rag_pipeline.rag.retrieval:retrieve --> rag_pipeline.catalog:retrieved_pages

	subgraph pipeline["Pipeline"]
		direction TB
		rag_pipeline.rag.annotation:annotate_documents(["annotate_documents"]):::node
		rag_pipeline.rag.evaluation:evaluate_answers(["evaluate_answers"]):::node
		rag_pipeline.rag.indexer:create_vector_index(["create_vector_index"]):::node
		rag_pipeline.rag.policies:generate_questions(["generate_questions"]):::node
		rag_pipeline.rag.question_answering:question_answering(["question_answering"]):::node
		rag_pipeline.rag.retrieval:filter_relevant(["filter_relevant"]):::node
		rag_pipeline.rag.retrieval:retrieve(["retrieve"]):::node
		rag_pipeline.catalog:index(index):::io1
		rag_pipeline.catalog:llm_answers(llm_answers):::io0
		rag_pipeline.catalog:llm_model(llm_model):::io5
		rag_pipeline.catalog:llm_vision_retrieval_model(llm_vision_retrieval_model):::io5
		rag_pipeline.catalog:metrics(metrics):::io2
		rag_pipeline.catalog:pdf_documents(pdf_documents):::io4
		rag_pipeline.catalog:pdfs_documents_annotated(pdfs_documents_annotated):::io4
		rag_pipeline.catalog:policies(policies):::io3
		rag_pipeline.catalog:questions(questions):::io0
		rag_pipeline.catalog:relevant_pages(relevant_pages):::io0
		rag_pipeline.catalog:retrieved_pages(retrieved_pages):::io0
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