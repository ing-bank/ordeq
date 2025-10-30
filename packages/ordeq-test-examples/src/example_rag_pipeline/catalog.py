from ordeq import IO
from typing import Any

policies = IO[Any]()  # PandasExcel(path=Path("policies.xlsx"))
llm_model = IO[Any]()  # SentenceTransformer(model="llm-model")
llm_vision_retrieval_model = IO[Any]()  # SentenceTransformer(model="vision-model")
pdf_documents = IO[Any]()  # PymupdfFile(path=Path("file1.pdf"))
retrieved_pages = IO[Any]()
relevant_pages = IO[Any]()
index = IO[Any]()  # FaissIndex(path=Path("documents.index"))
questions = IO[Any]()
metrics = IO[Any]()  # Pickle(path=Path("metrics.pkl"))
pdfs_documents_annotated = (
    IO[Any]()
)  # PymupdfFile(path=Path("file1_annotated.pdf"))
llm_answers = IO[Any]()
