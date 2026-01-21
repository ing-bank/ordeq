from dataclasses import dataclass
from typing import List, Union
import torch
import numpy as np
from .config import ModelConfig
from .loader import ModelLoader

@dataclass
class EmbeddingOutput:
    """Standardized output for embeddings."""
    embeddings: List[List[float]]
    model_name: str
    token_count: int

class EmbeddingsIO:
    """
    Main interface for generating text embeddings.
    Handles tokenization, forward pass, pooling, and normalization.
    """
    def __init__(self, config: Optional[ModelConfig] = None):
        self.config = config or ModelConfig()
        self.loader = ModelLoader(self.config)

    def generate(self, texts: Union[str, List[str]]) -> EmbeddingOutput:
        """
        Generates embeddings for a list of texts.
        
        Args:
            texts: A single string or a list of strings.
            
        Returns:
            EmbeddingOutput: Contains embeddings and metadata.
        """
        if isinstance(texts, str):
            texts = [texts]

        tokenizer, model = self.loader.load()

        # Tokenize
        inputs = tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=self.config.max_length,
            return_tensors="pt"
        )

        # Forward pass (no gradients for inference)
        with torch.no_grad():
            outputs = model(**inputs)

        # Mean Pooling - Take attention mask into account for correct averaging
        attention_mask = inputs['attention_mask']
        token_embeddings = outputs.last_hidden_state
        
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        embeddings = sum_embeddings / sum_mask

        # Normalize embeddings
        if self.config.normalize_embeddings:
            embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)

        # Convert to list of lists
        embeddings_list = embeddings.numpy().tolist()

        return EmbeddingOutput(
            embeddings=embeddings_list,
            model_name=self.config.model_name,
            token_count=inputs['input_ids'].numel()
        )
