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
			L00(IO):::io0
		end
	end

	IO0 --> generate_questions
	generate_questions --> IO1
	IO2 --> create_vector_index
	IO3 --> create_vector_index
	create_vector_index --> IO4
	IO4 --> retrieve
	IO1 --> retrieve
	IO3 --> retrieve
	retrieve --> IO5
	IO5 --> filter_relevant
	IO6 --> filter_relevant
	filter_relevant --> IO7
	IO1 --> question_answering
	IO7 --> question_answering
	IO6 --> question_answering
	question_answering --> IO8
	IO8 --> evaluate_answers
	IO6 --> evaluate_answers
	evaluate_answers --> IO9
	IO8 --> annotate_documents
	IO2 --> annotate_documents
	annotate_documents --> IO10

	subgraph pipeline["Pipeline"]
		direction TB
		generate_questions(["generate_questions"]):::node
		create_vector_index(["create_vector_index"]):::node
		retrieve(["retrieve"]):::node
		filter_relevant(["filter_relevant"]):::node
		question_answering(["question_answering"]):::node
		evaluate_answers(["evaluate_answers"]):::node
		annotate_documents(["annotate_documents"]):::node
		IO0(policies):::io0
		IO1(questions):::io0
		IO2(pdf_documents):::io0
		IO3(llm_vision_retrieval_model):::io0
		IO4(index):::io0
		IO5(retrieved_pages):::io0
		IO6(llm_model):::io0
		IO7(relevant_pages):::io0
		IO8(llm_answers):::io0
		IO9(metrics):::io0
		IO10(pdfs_documents_annotated):::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Typing

```text
packages/ordeq-viz/tests/resources/api/mermaid_rag.py:4: error: Skipping analyzing "rag_pipeline": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_rag.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```