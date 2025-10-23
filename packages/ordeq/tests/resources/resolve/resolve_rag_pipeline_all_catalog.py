from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)
import importlib

runnables = [
    importlib.import_module("rag_pipeline.rag.annotation"),
    importlib.import_module("rag_pipeline.rag.evaluation"),
    importlib.import_module("rag_pipeline.rag.indexer"),
    importlib.import_module("rag_pipeline.rag.policies"),
    importlib.import_module("rag_pipeline.rag.question_answering"),
    importlib.import_module("rag_pipeline.rag.retrieval"),
    importlib.import_module("rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(list(sorted(node.name for node in nodes)))
print(list(ios.keys()))

print(list(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables))))
