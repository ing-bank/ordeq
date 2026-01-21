import unittest
import numpy as np
from ordeq_transformers.config import ModelConfig
from ordeq_transformers.embeddings_io import EmbeddingsIO

class TestEmbeddings(unittest.TestCase):
    def setUp(self):
        # Use a very small model for testing to be fast
        self.config = ModelConfig(model_name="prajjwal1/bert-tiny", normalize_embeddings=True)
        self.io = EmbeddingsIO(self.config)

    def test_embedding_shape(self):
        text = "Hello world"
        output = self.io.generate(text)
        embeddings = output.embeddings
        
        self.assertEqual(len(embeddings), 1)
        # bert-tiny has hidden size 128
        self.assertEqual(len(embeddings[0]), 128)

    def test_determinism(self):
        text = "Consistency check"
        output1 = self.io.generate(text)
        output2 = self.io.generate(text)
        
        np.testing.assert_array_almost_equal(
            output1.embeddings[0], 
            output2.embeddings[0], 
            decimal=6
        )

    def test_batch_processing(self):
        texts = ["Hello", "World"]
        output = self.io.generate(texts)
        self.assertEqual(len(output.embeddings), 2)

if __name__ == '__main__':
    unittest.main()
