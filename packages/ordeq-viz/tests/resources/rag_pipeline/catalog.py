from pathlib import Path

from ordeq import IO
from ordeq_faiss import FaissIndex
from ordeq_files import Pickle
from ordeq_pandas import PandasExcel
from ordeq_pymupdf import PymupdfFile
from ordeq_sentence_transformers import SentenceTransformer


policies = PandasExcel(path=Path("policies.xlsx"))
llm_model = SentenceTransformer(model="llm-model")
llm_vision_retrieval_model = SentenceTransformer(model="vision-model")
pdf_documents = PymupdfFile(path=Path("file1.pdf"))
retrieved_pages = IO()
relevant_pages = IO()
index = FaissIndex(path=Path("documents.index"))
questions = IO()
metrics = Pickle(path=Path("metrics.pkl"))
pdfs_documents_annotated = PymupdfFile(path=Path("file1_annotated.pdf"))
llm_answers = IO()
