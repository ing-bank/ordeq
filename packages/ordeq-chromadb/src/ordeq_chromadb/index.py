import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from typing import Self  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Self

import chromadb
from ordeq import Input, Output

logger = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class ChromaDBIndex(Input[chromadb.Collection], Output[dict[str, Any]]):
    """IO to load from and save index data using ChromaDB. Creates a
    `chromadb.PersistentClient` by default during initialization and calls
    `client.get_collection` under the hood.

    Example usage:

    ```pycon
    >>> index = ChromaDBIndex.from_path(Path(...))
    >>> index.save({
    ...    "ids": [0, 1],
    ...    "embeddings": [
    ...       [0.1, 0.2, 0.3],
    ...       [0.4, 0.5, 0.6]],
    ...    "metadatas": [{"page_number": 1}, {"page_number": 2}],
    ...    "documents": ["Document 1", "Document 2"],
    ... }, collection_name="test_collection")
    >>> # collection_name should not be None
    >>> collection = index.load(
    ...    collection_name="test_collection"
    ... )
    >>> results = collection.query(
    ...    query_embeddings=[[0.1, 0.2, 0.3]],
    ...    n_results=2
    ... )
    ```
    """

    client: chromadb.ClientAPI

    @classmethod
    def from_path(cls, path: str | Path, **kwargs) -> Self:
        return cls(client=chromadb.PersistentClient(path=str(path), **kwargs))

    def load(
        self, collection_name: str = "", **load_options: Any
    ) -> chromadb.Collection:
        return self.client.get_collection(collection_name, **load_options)

    def save(
        self,
        data: dict[str, Any],
        collection_name: str = "",
        **save_options: Any,
    ) -> None:
        collection = self.client.get_or_create_collection(
            collection_name, **save_options
        )
        collection.add(**data)
