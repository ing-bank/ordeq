import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Self

import chromadb
from ordeq import Input, Output

logger = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class ChromaDBIndex(Input[chromadb.Collection], Output[dict[str, Any]]):
    client: chromadb.ClientAPI

    @classmethod
    def from_path(cls, path: str | Path, **kwargs) -> Self:
        return cls(client=chromadb.PersistentClient(path=str(path), **kwargs))

    def load(
        self, collection_name: str | None = None, **load_options: Any
    ) -> chromadb.Collection:
        return self.client.get_collection(collection_name, **load_options)

    def save(
        self,
        data: dict[str, Any],
        collection_name: str | None = None,
        **save_options: Any,
    ) -> None:
        collection = self.client.get_or_create_collection(
            collection_name, **save_options
        )
        collection.add(**data)


# usage index = ChromaDBIndex.from_path(Path(...))
