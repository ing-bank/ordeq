import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_rag_pipeline.rag.annotation"),
    importlib.import_module("example_rag_pipeline.rag.evaluation"),
    importlib.import_module("example_rag_pipeline.rag.indexer"),
    importlib.import_module("example_rag_pipeline.rag.policies"),
    importlib.import_module("example_rag_pipeline.rag.question_answering"),
    importlib.import_module("example_rag_pipeline.rag.retrieval"),
    importlib.import_module("example_rag_pipeline.catalog"),
]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(list(ios.keys()))

pprint(sorted(_resolve_runnables_to_nodes(*runnables)))
