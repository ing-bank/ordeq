from ordeq import IO

policies = IO()  # PandasExcel(path=Path("policies.xlsx"))
llm_model = IO()  # SentenceTransformer(model="llm-model")
llm_vision_retrieval_model = IO()  # SentenceTransformer(model="vision-model")
pdf_documents = IO()  # PymupdfFile(path=Path("file1.pdf"))
retrieved_pages = IO()
relevant_pages = IO()
index = IO()  # FaissIndex(path=Path("documents.index"))
questions = IO()
metrics = IO()  # Pickle(path=Path("metrics.pkl"))
pdfs_documents_annotated = (
    IO()
)  # PymupdfFile(path=Path("file1_annotated.pdf"))
llm_answers = IO()
