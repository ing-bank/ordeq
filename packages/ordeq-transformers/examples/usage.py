import sys
import os

# Add src to path so we can import the package without installing it
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from ordeq_transformers.config import ModelConfig
from ordeq_transformers.embeddings_io import EmbeddingsIO

def main():
    print("Initializing ordeq-transformers...")
    
    # 1. Configure
    # Using a small model for the example to run quickly
    config = ModelConfig(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        normalize_embeddings=True
    )
    
    # 2. Initialize IO
    embeddings_io = EmbeddingsIO(config)
    
    # 3. Generate Embeddings
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Artificial intelligence is transforming the world."
    ]
    
    print(f"Generating embeddings for {len(texts)} texts...")
    output = embeddings_io.generate(texts)
    
    # 4. Inspect Output
    print(f"\nModel used: {output.model_name}")
    print(f"Total tokens processed: {output.token_count}")
    
    for i, text in enumerate(texts):
        emb = output.embeddings[i]
        print(f"\nText: {text}")
        print(f"Embedding dimension: {len(emb)}")
        print(f"First 5 values: {emb[:5]}")

if __name__ == "__main__":
    main()
