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
class ChromaDBCollection(Input[chromadb.Collection], Output[dict[str, Any]]):
    """IO to load from and save collection using ChromaDB. Creates a
    `chromadb.PersistentClient` by default during initialization and calls
    `client.get_collection` under the hood.

    Example usage:

    ```pycon
    >>> index = ChromaDBCollection.from_path(
    ...     Path("/path/to/chromadb"),
    ...     name="test_collection"
    ... )  # doctest: +SKIP
    >>> index.save({
    ...    "ids": [0, 1],
    ...    "embeddings": [
    ...       [0.1, 0.2, 0.3],
    ...       [0.4, 0.5, 0.6]],
    ...    "metadatas": [{"page_number": 1}, {"page_number": 2}],
    ...    "documents": ["Document 1", "Document 2"],
    ... })  # doctest: +SKIP
    >>> # collection_name should not be None
    >>> collection = index.load()  # doctest: +SKIP
    >>> results = collection.query(
    ...    query_embeddings=[[0.1, 0.2, 0.3]],
    ...    n_results=2
    ... )  # doctest: +SKIP
    ```
    """

    client: chromadb.ClientAPI
    name: str

    @classmethod
    def from_path(cls, path: str | Path, name: str, **kwargs) -> Self:
        return cls(
            client=chromadb.PersistentClient(path=str(path), **kwargs),
            name=name,
        )

    def load(self, **load_options: Any) -> chromadb.Collection:
        return self.client.get_collection(self.name, **load_options)

    def save(self, data: dict[str, Any], **save_options: Any) -> None:
        collection = self.client.get_or_create_collection(
            self.name, **save_options
        )
        collection.add(**data)
