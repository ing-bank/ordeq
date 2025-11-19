import chromadb
import pytest
from ordeq_chromadb import ChromaDBIndex


@pytest.fixture
def data():
    return {
        "ids": ["1", "2", "3"],
        "embeddings": [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]],
        "metadatas": [
            {"text": "first"},
            {"text": "second"},
            {"text": "third"},
        ],
        "documents": ["Document 1", "Document 2", "Document 3"],
    }


def test_index(data, tmp_path):
    index = ChromaDBIndex.from_path(tmp_path / "chroma_db")
    index.save(data, collection_name="test_collection")

    collection = index.load(collection_name="test_collection")

    assert collection.count() == 3


def test_index_ephemeral_client(data):
    client = chromadb.EphemeralClient()

    index = ChromaDBIndex(client=client)
    index.save(data, collection_name="test_collection")

    collection = index.load(collection_name="test_collection")

    assert collection.count() == 3
